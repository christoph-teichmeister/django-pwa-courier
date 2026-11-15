import json
from http import HTTPStatus

import pytest

from pwa_courier.models import PushSubscription

URL = "/push/subscribe/"


def _body(status_type="subscribe", endpoint="https://push.example.com/abc"):
    return json.dumps(
        {
            "status_type": status_type,
            "browser": "safari",
            "user_agent": "iPhone",
            "subscription": {"endpoint": endpoint, "keys": {"auth": "a", "p256dh": "p"}},
        }
    )


def test_anonymous_gets_401(client):
    assert client.post(URL, _body(), content_type="application/json").status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_subscribe_creates_and_reconfirms(admin_client, admin_user):
    assert admin_client.post(URL, _body(), content_type="application/json").status_code == HTTPStatus.CREATED
    first = PushSubscription.objects.get(user=admin_user)

    assert admin_client.post(URL, _body(), content_type="application/json").status_code == HTTPStatus.CREATED
    second = PushSubscription.objects.get(user=admin_user)
    assert second.pk == first.pk
    assert second.last_confirmed_at > first.last_confirmed_at


@pytest.mark.django_db
def test_unsubscribe_deletes(admin_client, admin_user):
    admin_client.post(URL, _body(), content_type="application/json")

    response = admin_client.post(URL, _body("unsubscribe"), content_type="application/json")
    assert response.status_code == HTTPStatus.ACCEPTED
    assert not PushSubscription.objects.exists()


@pytest.mark.django_db
def test_user_who_opted_out_is_not_stored(admin_client, settings):
    settings.PWA_USER_WANTS_PUSH = "tests.helpers.never"

    admin_client.post(URL, _body(), content_type="application/json")

    assert not PushSubscription.objects.exists()


@pytest.mark.django_db
@pytest.mark.parametrize("body", ["not json", "[]", _body("bogus"), _body(endpoint="")])
def test_invalid_input_gets_400(admin_client, body):
    response = admin_client.post(URL, body, content_type="application/json")

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response["Content-Type"] == "application/json"
