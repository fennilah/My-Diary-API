from flask import request, url_for, jsonify


app = Flask_API(__name__)

@app.route('/', methods=['GET'])

def home_page():

@app.Errorhandler(404)

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
    url = "https://www.pivotaltracker.com/services/v5/projects"
    querystring = {"account_ids": str(id)}
    token_header = request.headers['X-TrackerToken']

    headers = {
        'X-TrackerToken': str(token_header),
        'Content-Type' : 'application/json'
        }
    response = request.request("GET", url, headers=headers, params=querystring)
    return response.text


@app.route('/api/v1/projects/create', methods=['POST'])

def createProject():
    projectName = request.json
    url = "https://www.pivotaltracker.com/services/v5/projects"
    token_header = request.headers['X-TrackerToken']

    payload = projectName
    headers = {
        'X-TrackerToken': str(token_header),
        }
    response = request.request("POST", url, data=payload, headers=headers)
    return response.text


@app.route('/api/v1/projects/<id>/stories/create', methods=['POST'])

def createStory(id):
    storyDetails = request.json
    story_url = "https://www.pivotaltracker.com/services/v5/projects/"+ id +"/stories"
    token_header = request.headers['X-TrackerToken']
    headers = {
        'X-TrackerToken': str(token_header)
    }
    response = request.request("POST", story_url, data=storyDetails, headers=headers)
    return response.text

@app.route('/api/v1/projects/<id>/stories/list', methods=['DELETE'])

def listProjectStories(id):
    url = "https://www.pivotaltracker.com/services/v5/projects/"+2186196+"/stories"
    token_header = request.headers['X-TrackerToken']
    headers = {
        'X-TrackerToken': str(token_header)
        }
    response = request.request("DELETE", url, headers=headers)
    return response.text

@app.route('/api/v1/projects/<pid>/stories/<sid>/edit', methods=['PUT'])

def editStory(pid, sid):
    story_url = "https://www.pivotaltracker.com/services/v5/projects/"+ 2186196 + "/stories/"+ 159223178
    edit = request.json
    token_header = request.headers['X-TrackerToken']
    headers = {
        'X-TrackerToken': str(token_header)
        }
    response = request.request("PUT", story_url, data=edit, headers=headers)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)
