from http import HTTPStatus


def test_handle_protocol_renders(client, settings):
    settings.PWA_WEB_PROTOCOL = "test"

    response = client.get("/handle-protocol/")

    assert response.status_code == HTTPStatus.OK
    assert b"web+test://" in response.content
