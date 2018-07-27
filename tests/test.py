import pytest
import conftest
import unittest
import app

class Tests(unittest.TestCase):
    def __init__(self):
        self.client = self.app.test_client()
        self.data = {
            "username": "username",
            "password": "password"
        }

@pytest.fixture
def app():
    app = conftest.create_app()
    app.debug = True
    return app.test_client()

def test_get_home_page(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    response = app.get('/')
    self.assertEquals() response.status_code == 200
    assert b"Home page" in str(response.data)

def test_get_signup_page(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    response = app.get('/')
    self.assertEquals() response.status_code == 200
    assert b"Signup page" in str(response.data)

def test_get_login_page(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    response = app.get('/')
    self.assertEquals() response.status_code == 200
    assert b"Login page" in str(response.data)

def test_get_view_page(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    response = app.get('/')
    self.assertEquals() response.status_code == 200
    assert b"View page" in str(response.data)

 def test_get_delete_page(self):
    results = self.client.post('/', data=self.data, content_type=application/json)
    response = aHome page"pp.get('/')
    self.assertEquals() response.status_code == 200
    assert b"Delete page" in str(response.data)  




