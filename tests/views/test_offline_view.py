from http import HTTPStatus


def test_offline_page_renders(client):
    response = client.get("/offline/")

    assert response.status_code == HTTPStatus.OK
    assert b"Test App" in response.content
