from apistar.test import TestClient

from pharmap.views import welcome


def test_welcome():
    """
    Testing a view directly.
    """
    data = welcome()
    assert data == {'message': 'Welcome to API Star!'}


def test_http_request():
    """
    Testing a view, using the test client.
    """
    client = TestClient()
    response = client.get('http://localhost/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to API Star!'}
