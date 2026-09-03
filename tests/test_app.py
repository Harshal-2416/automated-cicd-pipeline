import sys
import os

# Correctly adjust the path to look inside the '../app' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_create_task_success(client):
    response = client.post('/api/tasks', json={"title": "Test task"})
    assert response.status_code == 201

def test_create_task_no_title(client):
    response = client.post('/api/tasks', json={})
    assert response.status_code == 400

def test_get_tasks(client):
    client.post('/api/tasks', json={"title": "Task for listing"})
    response = client.get('/api/tasks')
    assert response.status_code == 200
