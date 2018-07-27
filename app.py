from flask import request, url_for, jsonify
from models import entry

app = Flask_API(__name__)

@app.route('/', methods=['GET'])

def Home_Page():

@app.errorhandler('/', methods=['404'])

def not_found(error=None):
    response = {
        'status' : 404,
        'message' : 'Request Not Found:' + request.url,
    }
    res = jsonify(response)
    res.status_code = 404
    return res

@app.route('/api/v1/entries/<id>', methods=['GET'])

def getAllEntry():
    querystring = {"account_id": str(id)}
    token_header = request.headers['X-TrackerToken']

    headers = {
        'X-TrackerToken': str(token_header),
        'Content-Type' : 'application/json'
        }
    response = request.request("GET", headers=headers, params=querystring)
    return response.text


@app.route('/api/v1/projects/create', methods=['POST'])

def getspecificEntry():
    entryName = request.json
    token_header = request.headers['X-TrackerToken']

    payload = entryName
    headers = {
        'X-TrackerToken': str(token_header),
        }
    response = request.request("POST", url, data=payload, headers=headers)
    return response.text


@app.route('/api/v1/projects/<id>/stories/create', methods=['POST'])

def createStory():
    storyDetails = request.json
    story_url = "https://www.pivotaltracker.com/services/v5/projects/"+ id +"/stories"
    token_header = request.headers['X-TrackerToken']
    headers = {
        'X-TrackerToken': str(token_header)
    }
    response = request.request("POST", story_url, data=storyDetails, headers=headers)
    return response.text

@app.route('/api/v1/projects/<id>/stories/list', methods=['DELETE'])

def listProjectStories():
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
