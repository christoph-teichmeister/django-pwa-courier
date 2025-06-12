# PWA-related settings
# ------------------------------------------------------------------------------
PWA_WEB_PROTOCOL: str = ""
PWA_SANITIZED_WEB_PROTOCOL: str = f"web+{PWA_WEB_PROTOCOL}"
PWA_CACHE_VERSION: str = ""
PWA_SERVICE_WORKER_DEBUG: bool = False

# PWA Manifest settings
# ------------------------------------------------------------------------------
PWA_MANIFEST_BACKGROUND_COLOR: str = "#ffffff"
PWA_MANIFEST_CATEGORIES: list = []
PWA_MANIFEST_DESCRIPTION: str = ""
PWA_MANIFEST_DIR: str = "auto"
PWA_MANIFEST_DISPLAY: str = "fullscreen"
PWA_MANIFEST_DISPLAY_OVERRIDE: list = ["window-controls-overlay", "fullscreen"]
PWA_MANIFEST_EDGE_SIDE_PANEL: dict = {}
PWA_MANIFEST_FEATURES: list = []
PWA_MANIFEST_ICONS: list = []
PWA_MANIFEST_ID: str = ""
PWA_MANIFEST_LANG: str = "en-US"
PWA_MANIFEST_LAUNCH_HANDLER: dict = {"client_mode": ["navigate-existing", "auto"]}
PWA_MANIFEST_NAME: str = ""
PWA_MANIFEST_ORIENTATION: str = "any"
PWA_MANIFEST_PROTOCOL_HANDLER_URL: str = "/handle-protocol?url=%s"
PWA_MANIFEST_PROTOCOL_HANDLERS: list = [
    {"protocol": PWA_SANITIZED_WEB_PROTOCOL, "url": PWA_MANIFEST_PROTOCOL_HANDLER_URL}
]
PWA_MANIFEST_RELATED_APPLICATIONS: list = []
PWA_MANIFEST_PREFER_RELATED_APPLICATIONS: bool = False
PWA_MANIFEST_SCREENSHOTS: list = []
PWA_MANIFEST_SCOPE: str = "/"
PWA_MANIFEST_SHORT_NAME: str = ""
PWA_MANIFEST_SPLASH_SCREENS: list = []
PWA_MANIFEST_START_URL: str = "/"
PWA_MANIFEST_THEME_COLOR: str = "#ffffff"

PWA_MANIFEST: dict = {
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
}

# Webpush-related settings
# ------------------------------------------------------------------------------
PWA_WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "",
    "VAPID_PRIVATE_KEY": "",
    "VAPID_ADMIN_EMAIL": "",
}
PWA_WEBPUSH_NOTIFICATION_CLASS = "apps.webpush.dataclasses.notification.Notification"
