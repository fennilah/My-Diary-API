import pytest
import conftest

@pytest.fixture
def app():
    app = conftest.create_app()
    app.debug = True
    return app.test_client()

def test_get_home_page(app):
    response = app.get('/')
    assert response.status_code == 200
    assert b"Home page" in response.data

def test_gets_all_project(app):
    response = app.get('api/v1/projects/accounts/1059760')
    assert response.status_code == 200
    assert len(response.data) > 0

def test_lists_stories_for_project(app):
    response = app.get('/api/v1/projects/2186195/stories/list')  
    assert response.status_code == 200
    assert len(response.data) > 0

def test_edit_story(app):
    response = app.put('/api/v1/projects/2186195/stories/159221866/edit')
    assert response.status_code == 200
    assert b"updated_at" in response.data  