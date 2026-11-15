from pwa_courier import settings


def get_sanitised_pwa_web_protocol() -> str:
    return f"web+{settings.get_pwa_web_protocol()}"
