import pytest
import sys
import os
import json
from datetime import datetime

# Add the python-apis directory to the path so we can import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python-apis'))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world_endpoint(client):
    """Test the basic hello world endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['message'] == 'Hello World!'
    assert data['version'] == '1.0.0'
    assert 'timestamp' in data
    
    # Verify timestamp format (ISO 8601)
    timestamp = data['timestamp']
    assert timestamp.endswith('Z')
    # Should be parseable as ISO format
    datetime.fromisoformat(timestamp[:-1])

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'OK'
    assert 'uptime' in data
    assert isinstance(data['uptime'], (int, float))
    assert data['uptime'] >= 0
    assert 'timestamp' in data
    
    # Verify timestamp format
    timestamp = data['timestamp']
    assert timestamp.endswith('Z')

def test_personalized_greeting_endpoint(client):
    """Test the personalized greeting endpoint"""
    test_names = ['John', 'Alice', 'Bob123', 'test-user']
    
    for name in test_names:
        response = client.get(f'/hello/{name}')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['message'] == f'Hello, {name}!'
        assert 'timestamp' in data
        
        # Verify timestamp format
        timestamp = data['timestamp']
        assert timestamp.endswith('Z')

def test_personalized_greeting_with_special_characters(client):
    """Test personalized greeting with URL-encoded characters"""
    response = client.get('/hello/John%20Doe')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['message'] == 'Hello, John Doe!'

def test_content_type_is_json(client):
    """Test that all endpoints return JSON content type"""
    endpoints = ['/', '/health', '/hello/test']
    
    for endpoint in endpoints:
        response = client.get(endpoint)
        assert response.content_type == 'application/json'

def test_nonexistent_endpoint_returns_404(client):
    """Test that nonexistent endpoints return 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_timestamp_consistency(client):
    """Test that timestamps are recent and consistently formatted"""
    import time
    
    before_request = time.time()
    response = client.get('/')
    after_request = time.time()
    
    data = json.loads(response.data)
    timestamp_str = data['timestamp']
    
    # Parse timestamp and convert to unix time
    timestamp_dt = datetime.fromisoformat(timestamp_str[:-1])  # Remove 'Z'
    timestamp_unix = timestamp_dt.timestamp()
    
    # Timestamp should be between before and after request times
    assert before_request <= timestamp_unix <= after_request

def test_uptime_increases_over_time(client):
    """Test that uptime increases between requests"""
    import time
    
    # First request
    response1 = client.get('/health')
    data1 = json.loads(response1.data)
    uptime1 = data1['uptime']
    
    # Wait a small amount
    time.sleep(0.1)
    
    # Second request
    response2 = client.get('/health')
    data2 = json.loads(response2.data)
    uptime2 = data2['uptime']
    
    # Second uptime should be greater than first
    assert uptime2 > uptime1

if __name__ == '__main__':
    pytest.main([__file__, '-v'])