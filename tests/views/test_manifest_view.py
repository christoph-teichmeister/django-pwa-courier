import json
from http import HTTPStatus


def test_manifest_returns_settings_manifest(client):
    response = client.get("/manifest.json")

    assert response.status_code == HTTPStatus.OK
    assert response["Content-Type"] == "application/manifest+json"
    assert json.loads(response.content)["name"] == "Test App"


def test_manifest_cache_busts_icons(client, settings):
    settings.PWA_ICON_VERSION = 7

    icons = json.loads(client.get("/manifest.json").content)["icons"]

    assert icons[0]["src"] == "/static/icon-192.png?v=7"
    assert settings.PWA_MANIFEST["icons"][0]["src"] == "/static/icon-192.png"  # settings not mutated
