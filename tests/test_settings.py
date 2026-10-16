from pwa_courier.settings import get_pwa_icon_version


def test_icon_version_plain_value_or_callable_path(settings):
    settings.PWA_ICON_VERSION = "1.2.3"
    assert get_pwa_icon_version() == "1.2.3"

    settings.PWA_ICON_VERSION = "tests.helpers.icon_version"
    assert get_pwa_icon_version() == "42"
