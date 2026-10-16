import json
import logging
from dataclasses import asdict, dataclass, field
from datetime import timedelta
from http import HTTPStatus

from django.utils.timezone import now
from pywebpush import WebPushException, webpush

from pwa_courier.models import PushSubscription
from pwa_courier.settings import get_pwa_manifest, get_pwa_webpush_settings, user_wants_push

logger = logging.getLogger(__name__)


@dataclass
class Notification:
    """A web push notification, see https://developer.mozilla.org/en-US/docs/Web/API/Notification

    Notification(head="Hi", body="Tap to open your profile", click_url="/profile/").send_to(user)
    """

    head: str
    body: str
    click_url: str = "/"
    icon: str | None = None
    badge: str | None = None
    image: str | None = None
    # Each action: {"action": "open", "title": "Open", "url": "/somewhere/"}
    actions: list[dict] = field(default_factory=list)
    vibrate: list[int] | None = None
    ttl: int = 1000

    def payload(self) -> str:
        default_icon = (get_pwa_manifest().get("icons") or [{}])[0].get("src")
        data = asdict(self)
        data.pop("ttl")
        data["icon"] = self.icon or default_icon
        data["badge"] = self.badge or default_icon
        data["actions"] = [{k: v for k, v in action.items() if k != "url"} for action in self.actions]
        data["data"] = {
            "notificationClickUrl": self.click_url,
            "actionClickUrls": [{"action": a.get("action", ""), "url": a.get("url", "")} for a in self.actions],
        }
        return json.dumps(data)

    def send_to(self, user) -> list[bool]:
        """One bool per subscription of the user: True if the push service accepted it."""
        if not user_wants_push(user):
            return []
        payload = self.payload()
        return [_send(subscription, payload, self.ttl) for subscription in user.push_subscriptions.all()]

    @staticmethod
    def was_delivered(results: list[bool]) -> bool:
        return any(results)


def has_only_stale_subscriptions(user) -> bool:
    """True if the user has no subscription confirmed within `PWA_WEBPUSH["STALE_AFTER_DAYS"]`."""
    threshold = now() - timedelta(days=get_pwa_webpush_settings()["STALE_AFTER_DAYS"])
    return not user.push_subscriptions.filter(last_confirmed_at__gte=threshold).exists()


def _send(subscription: PushSubscription, payload: str, ttl: int) -> bool:
    try:
        webpush(
            subscription_info={
                "endpoint": subscription.endpoint,
                "keys": {"p256dh": subscription.p256dh, "auth": subscription.auth},
            },
            data=payload,
            ttl=ttl,
            **_vapid_kwargs(),
        )
    except WebPushException as e:
        status = getattr(e.response, "status_code", None)
        if status in (HTTPStatus.NOT_FOUND, HTTPStatus.GONE):
            # The browser dropped the subscription, it will never work again.
            subscription.delete()
        else:
            logger.warning("Web push to subscription %s failed: %s", subscription.pk, e)
        return False
    return True


def _vapid_kwargs() -> dict:
    webpush_settings = get_pwa_webpush_settings()
    if not webpush_settings["VAPID_PRIVATE_KEY"]:
        return {}
    return {
        "vapid_private_key": webpush_settings["VAPID_PRIVATE_KEY"],
        "vapid_claims": {"sub": f"mailto:{webpush_settings['VAPID_ADMIN_EMAIL']}"},
    }
