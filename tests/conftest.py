import os

from flask import Flask,jsonify
from random import randint
import requests


def create_app(config=None):
    app = Flask_API(__name__)
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

@app.route("/")
def homePage():
        return "Home page"

@app.route('/api/v1/projects/accounts/<id>', methods=['GET'])
def getsEntries(id):
        url = "http://localhost:5000/api/v1/projects/accounts/"+ id
        headers = {
            'X-TrackerToken': "75497933ff68780e86ce333b790951b0"
            }
        response = requests.request("GET", url, headers=headers)
        return response.text

@app.route('/api/v1/projects/<id>/stories/list', methods=['GET'])
def listEntries(id):
        url = "http://localhost:5000/api/v1/projects/"+id+"/stories"
        headers = {
            'X-TrackerToken': '75497933ff68780e86ce333b790951b0'
            }
        response = requests.request("GET", url, headers=headers)
        return response.text
    
@app.route('/api/v1/projects/<pid>/stories/<sid>/edit', methods=['DELETE'])
def deleteEntries(pid,sid):
        storyUrl = "http://localhost:5000/api/v1/projects/"+ pid + "/stories/"+ sid +"/edit"
        mid = str(randint(5,100))
        payload = "{\"name\":\"Pytest Edit "+ mid +"\"}"
        headers = {
            'X-TrackerToken': '75497933ff68780e86ce333b790951b0'
            }
        response = requests.request("PUT", storyUrl, data=payload, headers=headers)
        return response.text


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app. = create_app()
    app.run(host="0.0.0.0", port=8000)
