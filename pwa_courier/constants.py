def get_sanitised_pwa_web_protocol() -> str:
    from pwa_courier import settings as pwa_courier_settings

    return f"web+{pwa_courier_settings.get_pwa_web_protocol()}"
