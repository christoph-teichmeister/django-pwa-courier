import json
from datetime import timedelta
from unittest import mock

import pytest
from django.utils.timezone import now
from pywebpush import WebPushException

from pwa_courier.models import PushSubscription
from pwa_courier.notifications import Notification, has_only_stale_subscriptions


@pytest.fixture
def subscription(admin_user):
    return PushSubscription.objects.create(
        user=admin_user, browser="safari", endpoint="https://push.example.com/1", auth="a", p256dh="p"
    )


def test_payload_defaults_icon_and_moves_action_urls():
    notification = Notification(
        head="Hi", body="There", click_url="/x/", actions=[{"action": "open", "title": "Open", "url": "/y/"}]
    )

    payload = json.loads(notification.payload())

    assert payload["head"] == "Hi"
    assert payload["icon"] == payload["badge"] == "/static/icon-192.png"
    assert payload["actions"] == [{"action": "open", "title": "Open"}]
    assert payload["data"] == {"notificationClickUrl": "/x/", "actionClickUrls": [{"action": "open", "url": "/y/"}]}
    assert "ttl" not in payload


@pytest.mark.django_db
def test_send_to_delivers_with_vapid(settings, admin_user, subscription):
    settings.PWA_WEBPUSH = {**settings.PWA_WEBPUSH, "VAPID_PRIVATE_KEY": "priv"}

    with mock.patch("pwa_courier.notifications.webpush") as webpush:
        results = Notification(head="Hi", body="There").send_to(admin_user)

    assert results == [True]
    assert Notification.was_delivered(results)
    kwargs = webpush.call_args.kwargs
    assert kwargs["subscription_info"]["endpoint"] == "https://push.example.com/1"
    assert kwargs["vapid_claims"] == {"sub": "mailto:admin@example.com"}


@pytest.mark.django_db
@pytest.mark.parametrize(("status", "kept"), [(410, False), (404, False), (500, True)])
def test_failed_send_returns_false_and_drops_dead_subscriptions(admin_user, subscription, status, kept):
    error = WebPushException("nope", response=mock.Mock(status_code=status))

    with mock.patch("pwa_courier.notifications.webpush", side_effect=error):
        results = Notification(head="Hi", body="There").send_to(admin_user)

    assert results == [False]
    assert PushSubscription.objects.filter(pk=subscription.pk).exists() is kept


@pytest.mark.django_db
def test_send_to_skips_users_who_opted_out(settings, admin_user, subscription):
    settings.PWA_USER_WANTS_PUSH = "tests.helpers.never"

    with mock.patch("pwa_courier.notifications.webpush") as webpush:
        assert Notification(head="Hi", body="There").send_to(admin_user) == []
    webpush.assert_not_called()


@pytest.mark.django_db
def test_has_only_stale_subscriptions(admin_user, subscription):
    assert not has_only_stale_subscriptions(admin_user)

    PushSubscription.objects.update(last_confirmed_at=now() - timedelta(days=11))
    assert has_only_stale_subscriptions(admin_user)

    PushSubscription.objects.all().delete()
    assert has_only_stale_subscriptions(admin_user)
