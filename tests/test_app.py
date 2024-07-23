from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_hello_world():
    client = TestClient(app)  # Arrange  - Organização

    response = client.get('/')  # Act - Ação

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello world'}
