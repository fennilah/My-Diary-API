import pytest

BASE_URL = 'api/v1'

SAMPLE_TEST_DATA = {
    'id': 100,
    'title': u'Shopping',
    'text': u'I went shopping',
}


@pytest.fixture
def app():
    app = app()
    app.debug = True
    return app.test_client()


def test_home_page(app):
    response = app.get('/')
    assert response.status_code == 200
    assert 'Home Page' in str(response.data)    


def test_add_stories(app):
   response = app.post('{}/stories?id={}&title={}&text={}'.format(BASE_URL, SAMPLE_TEST_DATA['id'], SAMPLE_TEST_DATA['title'], SAMPLE_TEST_DATA['text']))
   assert response.status_code == 200
   assert 'updated_at' in str(response.data)
 

def test_edit_stories(app):
   response = app.put('{}/stories/100?title=Shopping'.format(BASE_URL))
   assert response.status_code == 200
   assert 'walking' in str(response.data)
   assert '100 walking I went shopping' in str(response.data)


def test_delete_entries(app):
   response = app.put('{}/stories?id={}'.format(BASE_URL, SAMPLE_TEST_DATA['id']))
   assert response.status_code == 200
   assert 'entries deleted' in str(response.data)  


def test_list_entries(app):
   response = app.get('{}/entries'.format(BASE_URL))
   assert response.status_code == 200
   assert 'list of entries' in str(response.data)>0    






