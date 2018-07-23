
import os,requests

from flask import Flask,jsonify
from random import randint


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    @app.route("/")
    def home_page():
        return "Home page"

    @app.route('/api/v1/projects/accounts/<id>', methods=['GET'])
    def getsProjects(id):
        url = "http://localhost:5000/api/v1/projects/accounts/"+ id
        headers = {
            'X-TrackerToken': "815f1d584770a6144ad5b361145944c0"
            }
        response = requests.request("GET", url, headers=headers)
        return response.text

    @app.route('/api/v1/projects/<id>/stories/list', methods=['GET'])
    def listProjectStories(id):
        url = "http://localhost:5000/api/v1/projects/"+id+"/stories"
        headers = {
            'X-TrackerToken': '815f1d584770a6144ad5b361145944c0'
            }
        response = requests.request("GET", url, headers=headers)
        return response.text
    
    @app.route('/api/v1/projects/<pid>/stories/<sid>/edit', methods=['PUT'])
    def editStory(pid,sid):
        storyUrl = "http://localhost:5000/api/v1/projects/"+ pid + "/stories/"+ sid +"/edit"
        mid = str(randint(5,100))
        payload = "{\"name\":\"Pytest Edit "+ mid +"\"}"
        headers = {
            'X-TrackerToken': '815f1d584770a6144ad5b361145944c0'
            }
        response = requests.request("PUT", storyUrl, data=payload, headers=headers)
        return response.text

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)