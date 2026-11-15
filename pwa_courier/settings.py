from django.conf import settings
from django.utils.module_loading import import_string


def get_pwa_manifest() -> dict:
    return getattr(settings, "PWA_MANIFEST", {})


def get_pwa_webpush_settings() -> dict:
    return {
        "VAPID_PUBLIC_KEY": "",
        "VAPID_PRIVATE_KEY": "",
        "VAPID_ADMIN_EMAIL": "",
        "STALE_AFTER_DAYS": 10,
        **getattr(settings, "PWA_WEBPUSH", {}),
    }


def get_pwa_service_worker_debug() -> bool:
    return getattr(settings, "PWA_SERVICE_WORKER_DEBUG", False)


def get_pwa_service_worker_template() -> str:
    """Apps extend the package worker by pointing this at their own template that `{% extends %}` it."""
    return getattr(settings, "PWA_SERVICE_WORKER_TEMPLATE", "django_pwa_courier/pwa/serviceworker.js")


def get_pwa_cache_version() -> str:
    return str(getattr(settings, "PWA_CACHE_VERSION", "1"))


def get_pwa_icon_version() -> str:
    """Appended as `?v=` to icon URLs. A value or a dotted path to a callable (e.g. one that reads the DB)."""
    value = getattr(settings, "PWA_ICON_VERSION", "")
    if isinstance(value, str) and "." in value and not value.replace(".", "").isdigit():
        try:
            value = import_string(value)()
        except ImportError:
            pass  # a plain version string like "1.0.0-beta"
    return str(value)


def get_pwa_web_protocol() -> str:
    return getattr(settings, "PWA_WEB_PROTOCOL", "")


def user_wants_push(user) -> bool:
    """`PWA_USER_WANTS_PUSH` may be a dotted path to `callable(user) -> bool`."""
    if path := getattr(settings, "PWA_USER_WANTS_PUSH", ""):
        return import_string(path)(user)
    return getattr(user, "wants_to_receive_webpush_notifications", True)
