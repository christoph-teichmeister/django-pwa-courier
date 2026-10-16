from django.urls import include, path


def never(user) -> bool:
    return False


def icon_version() -> int:
    return 42


# URLconf without the admin, for the service worker's admin-less fallback
urlpatterns = [path("", include("pwa_courier.urls"))]
