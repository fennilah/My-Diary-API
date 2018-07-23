
from flask import request, url_for, jsonify
from flask_api import FlaskAPI


app = FlaskAPI(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Home page'

#  Error Handler 404
@app.errorhandler(404)
def not_found(error=None):
    response = {
        'status' : 404,
        'message' : 'Request Not Found:' + request.url,
    }
    res = jsonify(response)
    res.status_code = 404
    return res


@app.route('/api/v1/projects/accounts/<id>', methods=['GET'])
def getAllProjects(id):
    url = "https://www.pivotaltracker.com/n/projects/2186196"
    querystring = {"account_ids": str(id)}
    token_header = request.headers['75497933ff68780e86ce333b790951b0']

    headers = {
        '75497933ff68780e86ce333b790951b0': str(token_header),
        'Content-Type' : 'application/json'
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

@app.route('/api/v1/projects/create', methods=['POST'])
def createProject():
    mydiary = request.json
    url = "https://www.pivotaltracker.com/n/projects/2186196"
    token_header = request.headers['75497933ff68780e86ce333b790951b0']

    payload = mydiary
    headers = {
        '75497933ff68780e86ce333b790951b0': str(token_header),
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


@app.route('/api/v1/projects/<id>/stories/create', methods=['POST'])
def createStory(id):
    storyDetails = request.json
    story_url = "https://www.pivotaltracker.com/n/projects/2186196"+ id +"/stories"
    token_header = request.headers['75497933ff68780e86ce333b790951b0']
    headers = {
        '75497933ff68780e86ce333b790951b0': str(token_header)
    }
    response = requests.request("POST", story_url, data=storyDetails, headers=headers)
    return response.text


@app.route('/api/v1/projects/<id>/stories/list', methods=['GET'])
def listProjectStories(id):
    url = "https://www.pivotaltracker.com/n/projects/2186196"+id+"/stories"
    token_header = request.headers['75497933ff68780e86ce333b790951b0']
    headers = {
        '75497933ff68780e86ce333b790951b0': str(token_header)
        }
    response = requests.request("GET", url, headers=headers)
    return response.text


@app.route('/api/v1/projects/<pid>/stories/<sid>/edit', methods=['PUT'])
def editStory(pid, sid):
    story_url = "https://www.pivotaltracker.com/n/projects/2186196"+ pid + "/stories/"+ sid
    edit = request.json
    token_header = request.headers['75497933ff68780e86ce333b790951b0']
    headers = {
        '75497933ff68780e86ce333b790951b0': str(token_header)
        }
    response = requests.request("PUT", story_url, data=edit, headers=headers)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)
