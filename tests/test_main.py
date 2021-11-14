import pytest
from main import app


@pytest.fixture()
def client():
    '''Client for testing routes'''

    with app.test_client() as client:
        yield client


def test_index(client):
    '''Test index route for 200 status and text in response'''

    response = client.get('/')
    assert b'Hello!' in response.data
    assert response.status_code == 200
