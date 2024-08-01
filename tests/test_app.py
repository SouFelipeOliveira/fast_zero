from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get("/")  # Act - Ação

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testusername",
            "email": "test@gmail.com",
            "password": "test",
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        "id": 1,
        "username": "testusername",
        "email": "test@gmail.com",
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "user": [{"id": 1, "username": "testusername", "email": "test@gmail.com"}]
    }


def test_hello_world_html(client, html_response):
    response = client.get("/HelloWorldHtml/")
    assert response.status_code == HTTPStatus.OK
    assert response.text == html_response
