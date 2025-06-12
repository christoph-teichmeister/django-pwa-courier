from django.conf import settings

# PWA-related Settings
# ------------------------------------------------------------------------------
PWA_WEB_PROTOCOL: str = getattr(settings, "PWA_WEB_PROTOCOL", "")
PWA_SANITIZED_WEB_PROTOCOL: str = f"web+{PWA_WEB_PROTOCOL}"
PWA_CACHE_VERSION: str = getattr(settings, "PWA_CACHE_VERSION", "")
PWA_SERVICE_WORKER_DEBUG: bool = getattr(settings, "DEBUG", "")

# PWA Manifest Settings
# ------------------------------------------------------------------------------
PWA_MANIFEST_BACKGROUND_COLOR: str = getattr(settings, "PWA_MANIFEST_BACKGROUND_COLOR", "#ffffff")
PWA_MANIFEST_CATEGORIES: list = getattr(settings, "PWA_MANIFEST_CATEGORIES", [])
PWA_MANIFEST_DESCRIPTION: str = getattr(settings, "PWA_MANIFEST_DESCRIPTION", "")
PWA_MANIFEST_DIR: str = getattr(settings, "PWA_MANIFEST_DIR", "auto")
PWA_MANIFEST_DISPLAY: str = getattr(settings, "PWA_MANIFEST_DISPLAY", "fullscreen")
PWA_MANIFEST_DISPLAY_OVERRIDE: list = getattr(
    settings, "PWA_MANIFEST_DISPLAY_OVERRIDE", ["window-controls-overlay", "fullscreen"]
)
PWA_MANIFEST_EDGE_SIDE_PANEL: dict = getattr(settings, "PWA_MANIFEST_EDGE_SIDE_PANEL", {})
PWA_MANIFEST_FEATURES: list = getattr(settings, "PWA_MANIFEST_FEATURES", [])
PWA_MANIFEST_ICONS: list = getattr(settings, "PWA_MANIFEST_ICONS", [])
PWA_MANIFEST_ID: str = getattr(settings, "PWA_MANIFEST_ID", "")
PWA_MANIFEST_LANG: str = getattr(settings, "PWA_MANIFEST_LANG", "en-US")
PWA_MANIFEST_LAUNCH_HANDLER: dict = getattr(
    settings, "PWA_MANIFEST_LAUNCH_HANDLER", {"client_mode": ["navigate-existing", "auto"]}
)
PWA_MANIFEST_NAME: str = getattr(settings, "PWA_MANIFEST_NAME", "")
PWA_MANIFEST_ORIENTATION: str = getattr(settings, "PWA_MANIFEST_ORIENTATION", "any")
PWA_MANIFEST_PROTOCOL_HANDLER_URL: str = getattr(
    settings, "PWA_MANIFEST_PROTOCOL_HANDLER_URL", "/handle-protocol?url=%s"
)
PWA_MANIFEST_PROTOCOL_HANDLERS: list = getattr(
    settings,
    "PWA_MANIFEST_PROTOCOL_HANDLERS",
    [{"protocol": PWA_SANITIZED_WEB_PROTOCOL, "url": PWA_MANIFEST_PROTOCOL_HANDLER_URL}],
)
PWA_MANIFEST_RELATED_APPLICATIONS: list = getattr(settings, "PWA_MANIFEST_RELATED_APPLICATIONS", [])
PWA_MANIFEST_PREFER_RELATED_APPLICATIONS: bool = getattr(settings, "PWA_MANIFEST_PREFER_RELATED_APPLICATIONS", False)
PWA_MANIFEST_SCREENSHOTS: list = getattr(settings, "PWA_MANIFEST_SCREENSHOTS", [])
PWA_MANIFEST_SCOPE: str = getattr(settings, "PWA_MANIFEST_SCOPE", "/")
PWA_MANIFEST_SHORT_NAME: str = getattr(settings, "PWA_MANIFEST_SHORT_NAME", "")
PWA_MANIFEST_SPLASH_SCREENS: list = getattr(settings, "PWA_MANIFEST_SPLASH_SCREENS", [])
PWA_MANIFEST_START_URL: str = getattr(settings, "PWA_MANIFEST_START_URL", "/")
PWA_MANIFEST_THEME_COLOR: str = getattr(settings, "PWA_MANIFEST_THEME_COLOR", "#ffffff")

PWA_MANIFEST: dict = getattr(
    settings,
    "PWA_MANIFEST",
    {
        "background_color": PWA_MANIFEST_BACKGROUND_COLOR,
        "categories": PWA_MANIFEST_CATEGORIES,
        "description": PWA_MANIFEST_DESCRIPTION,
        "dir": PWA_MANIFEST_DIR,
        "display": PWA_MANIFEST_DISPLAY,
        "display_override": PWA_MANIFEST_DISPLAY_OVERRIDE,
        "edge_side_panel": PWA_MANIFEST_EDGE_SIDE_PANEL,
        "features": PWA_MANIFEST_FEATURES,
        "icons": PWA_MANIFEST_ICONS,
        "id": PWA_MANIFEST_ID,
        "lang": PWA_MANIFEST_LANG,
        "launch_handler": PWA_MANIFEST_LAUNCH_HANDLER,
        "name": PWA_MANIFEST_NAME,
        "orientation": PWA_MANIFEST_ORIENTATION,
        "protocol_handlers": PWA_MANIFEST_PROTOCOL_HANDLERS,
        "related_applications": PWA_MANIFEST_RELATED_APPLICATIONS,
        "prefer_related_applications": PWA_MANIFEST_PREFER_RELATED_APPLICATIONS,
        "screenshots": PWA_MANIFEST_SCREENSHOTS,
        "scope": PWA_MANIFEST_SCOPE,
        "short_name": PWA_MANIFEST_SHORT_NAME,
        "splash_screens": PWA_MANIFEST_SPLASH_SCREENS,
        "start_url": PWA_MANIFEST_START_URL,
        "theme_color": PWA_MANIFEST_THEME_COLOR,
    },
)

# WEBPUSH
# ------------------------------------------------------------------------------
PWA_WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": getattr(settings, "PWA_VAPID_PUBLIC_KEY", ""),
    "VAPID_PRIVATE_KEY": getattr(settings, "PWA_VAPID_PRIVATE_KEY", ""),
    "VAPID_ADMIN_EMAIL": getattr(settings, "PWA_VAPID_ADMIN_EMAIL", ""),
}
PWA_WEBPUSH_NOTIFICATION_CLASS = "apps.webpush.dataclasses.notification.Notification"
