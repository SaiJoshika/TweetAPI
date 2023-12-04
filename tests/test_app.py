import sys
sys.path.append('C:\\Users\\saijo\\TweetAPI')
import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_tweet_success(client):
    data = {'text': 'This is a test tweet'}
    response = client.post('/tweet', json=data)
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'Tweet created successfully'

def test_create_tweet_missing_text(client):
    data = {}  # Missing 'text' field
    response = client.post('/tweet', json=data)
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == "Missing required field: 'text'"

