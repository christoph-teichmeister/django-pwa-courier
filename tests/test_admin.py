from http import HTTPStatus

import pytest

from pwa_courier.models import PushSubscription


@pytest.mark.django_db
def test_admin_lists_subscriptions_but_cannot_add(admin_client, admin_user):
    PushSubscription.objects.create(user=admin_user, browser="safari", endpoint="https://push.example.com/1")

    changelist = admin_client.get("/admin/pwa_courier/pushsubscription/")
    add = admin_client.get("/admin/pwa_courier/pushsubscription/add/")

    assert changelist.status_code == HTTPStatus.OK
    assert f"{admin_user} (safari)" in changelist.content.decode()
    assert add.status_code == HTTPStatus.FORBIDDEN
