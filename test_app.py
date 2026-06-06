import pytest
from main import app

@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_default_gif(client):
    """Test if the default GIF route returns correctly"""
    response = client.get('/default_gif')
    # Assert that the returned status code is 200
    assert response.status_code == 200

def test_feedback_post(client):
    """Test if submitting feedback works correctly"""
    mock_data = {"gif_id": "test-123", "rating": 5, "comment": "Great!"}
    response = client.post('/feedback', json=mock_data)
    # Assert that the returned JSON data has 'status' field with value 'ok'
    assert response.get_json()['status'] == 'ok'