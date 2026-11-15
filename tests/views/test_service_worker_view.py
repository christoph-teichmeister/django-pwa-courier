from http import HTTPStatus


def test_service_worker_is_served_as_javascript(client):
    response = client.get("/serviceworker.js")

    assert response.status_code == HTTPStatus.OK
    assert response["Content-Type"] == "text/javascript"
    assert response["Service-Worker-Allowed"] == "/"
    content = response.content.decode()
    assert r'const cachePrefix = "testapp\u002Dcache\u002D"' in content
    assert r'"/static/icon\u002D192.png"' in content
    assert 'const offlineUrl = "/offline/"' in content
    assert 'adminUrl = "/admin/"' in content
    assert 'addEventListener("push"' in content


def test_service_worker_template_can_be_swapped(client, settings, tmp_path):
    (tmp_path / "sw.js").write_text(
        '{% extends "django_pwa_courier/pwa/serviceworker.js" %}{% block extra %}// app extra{% endblock %}'
    )
    settings.TEMPLATES = [{**settings.TEMPLATES[0], "DIRS": [tmp_path]}]
    settings.PWA_SERVICE_WORKER_TEMPLATE = "sw.js"

    content = client.get("/serviceworker.js").content.decode()

    assert "// app extra" in content
    assert "notificationclick" in content


def test_service_worker_without_admin(client, settings):
    settings.ROOT_URLCONF = "tests.helpers"

    content = client.get("/serviceworker.js").content.decode()

    assert 'adminUrl = ""' in content
