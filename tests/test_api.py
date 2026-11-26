
import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_obtener_publicacion():
    """Verifica la consulta de una publicación mediante GET."""

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    assert "body" in data


@pytest.mark.api
def test_crear_publicacion():
    """Verifica la creación de una publicación mediante POST."""

    payload = {
        "title": "Prueba automatizada",
        "body": "Publicacion creada desde Pytest",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

@pytest.mark.api
def test_eliminar_publicacion():
    """Verifica la eliminación de una publicación mediante DELETE."""

    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data == {}

@pytest.mark.api
def test_publicacion_inexistente():
    """Verifica la respuesta ante una publicación inexistente."""

    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=10
    )

    assert response.status_code == 404
    assert response.json() == {}
