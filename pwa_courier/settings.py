from django.conf import settings


# PWA-related settings
# ------------------------------------------------------------------------------
def get_pwa_web_protocol() -> str:
    return getattr(settings, "PWA_WEB_PROTOCOL", "")


def get_pwa_cache_version() -> str:
    return getattr(settings, "PWA_CACHE_VERSION", "")


def get_pwa_service_worker_debug() -> bool:
    return getattr(settings, "PWA_SERVICE_WORKER_DEBUG", False)


# PWA Manifest settings
# ------------------------------------------------------------------------------
def get_pwa_manifest_background_color() -> str:
    return getattr(settings, "PWA_MANIFEST_BACKGROUND_COLOR", "#ffffff")


def get_pwa_manifest_categories() -> list:
    return getattr(settings, "PWA_MANIFEST_CATEGORIES", [])


def get_pwa_manifest_description() -> str:
    return getattr(settings, "PWA_MANIFEST_DESCRIPTION", "")


def get_pwa_manifest_dir() -> str:
    return getattr(settings, "PWA_MANIFEST_DIR", "auto")


def get_pwa_manifest_display() -> str:
    return getattr(settings, "PWA_MANIFEST_DISPLAY", "fullscreen")


def get_pwa_manifest_display_override() -> list:
    return getattr(settings, "PWA_MANIFEST_DISPLAY_OVERRIDE", ["window-controls-overlay", "fullscreen"])


def get_pwa_manifest_edge_side_panel() -> dict:
    return getattr(settings, "PWA_MANIFEST_EDGE_SIDE_PANEL", {})


def get_pwa_manifest_features() -> list:
    return getattr(settings, "PWA_MANIFEST_FEATURES", [])


def get_pwa_manifest_icons() -> list:
    return getattr(settings, "PWA_MANIFEST_ICONS", [])


def get_pwa_manifest_id() -> str:
    """
    Cache key to store registered handlers in.
    """
    return getattr(settings, "PWA_MANIFEST_ID", "")


def get_pwa_manifest_lang() -> str:
    return getattr(settings, "PWA_MANIFEST_LANG", "en-US")


def get_pwa_manifest_launch_handler() -> dict:
    return getattr(settings, "PWA_MANIFEST_LAUNCH_HANDLER", {"client_mode": ["navigate-existing", "auto"]})


def get_pwa_manifest_name() -> str:
    return getattr(settings, "PWA_MANIFEST_NAME", "")


def get_pwa_manifest_orientation() -> str:
    return getattr(settings, "PWA_MANIFEST_ORIENTATION", "any")


def get_pwa_manifest_protocol_handler_url() -> str:
    return getattr(settings, "PWA_MANIFEST_PROTOCOL_HANDLER_URL", "/handle-protocol?url=%s")


def get_pwa_manifest_protocol_handlers() -> list:
    from pwa_courier.constants import get_sanitised_pwa_web_protocol

    protocol_handler_url = get_pwa_manifest_protocol_handler_url()
    sanitised_protocol = get_sanitised_pwa_web_protocol()
    default = [{"protocol": sanitised_protocol, "url": protocol_handler_url}]
    return getattr(settings, "PWA_MANIFEST_PROTOCOL_HANDLERS", default)


def get_pwa_manifest_related_applications() -> list:
    return getattr(settings, "PWA_MANIFEST_RELATED_APPLICATIONS", [])


def get_pwa_manifest_prefer_related_applications() -> bool:
    return getattr(settings, "PWA_MANIFEST_PREFER_RELATED_APPLICATIONS", False)


def get_pwa_manifest_screenshots() -> list:
    return getattr(settings, "PWA_MANIFEST_SCREENSHOTS", [])


def get_pwa_manifest_scope() -> str:
    return getattr(settings, "PWA_MANIFEST_SCOPE", "/")


def get_pwa_manifest_short_name() -> str:
    return getattr(settings, "PWA_MANIFEST_SHORT_NAME", "")


def get_pwa_manifest_splash_screens() -> list:
    return getattr(settings, "PWA_MANIFEST_SPLASH_SCREENS", [])


def get_pwa_manifest_start_url() -> str:
    return getattr(settings, "PWA_MANIFEST_START_URL", "/")


def get_pwa_manifest_theme_color() -> str:
    return getattr(settings, "PWA_MANIFEST_THEME_COLOR", "#ffffff")


def get_pwa_manifest() -> dict:
    return getattr(
        settings,
        "PWA_MANIFEST",
        {
            "background_color": get_pwa_manifest_background_color(),
            "categories": get_pwa_manifest_categories(),
            "description": get_pwa_manifest_description(),
            "dir": get_pwa_manifest_dir(),
            "display": get_pwa_manifest_display(),
            "display_override": get_pwa_manifest_display_override(),
            "edge_side_panel": get_pwa_manifest_edge_side_panel(),
            "features": get_pwa_manifest_features(),
            "icons": get_pwa_manifest_icons(),
            "id": get_pwa_manifest_id(),
            "lang": get_pwa_manifest_lang(),
            "launch_handler": get_pwa_manifest_launch_handler(),
            "name": get_pwa_manifest_name(),
            "orientation": get_pwa_manifest_orientation(),
            "protocol_handlers": get_pwa_manifest_protocol_handlers(),
            "related_applications": get_pwa_manifest_related_applications(),
            "prefer_related_applications": get_pwa_manifest_prefer_related_applications(),
            "screenshots": get_pwa_manifest_screenshots(),
            "scope": get_pwa_manifest_scope(),
            "short_name": get_pwa_manifest_short_name(),
            "splash_screens": get_pwa_manifest_splash_screens(),
            "start_url": get_pwa_manifest_start_url(),
            "theme_color": get_pwa_manifest_theme_color(),
        },
    )


# For backward compatibility
PWA_MANIFEST = get_pwa_manifest()


# Webpush-related settings
# ------------------------------------------------------------------------------
def get_pwa_webpush_settings() -> dict:
    return getattr(
        settings,
        "PWA_WEBPUSH_SETTINGS",
        {
            "VAPID_PUBLIC_KEY": "",
            "VAPID_PRIVATE_KEY": "",
            "VAPID_ADMIN_EMAIL": "",
        },
    )


def get_pwa_webpush_notification_class() -> str:
    return getattr(settings, "PWA_WEBPUSH_NOTIFICATION_CLASS", "apps.webpush.dataclasses.notification.Notification")
