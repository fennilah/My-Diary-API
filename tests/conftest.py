import os

from flask import Flask,jsonify
from random import randint


def create_app(config=None):
    app = Flask_API(__name__)
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

def homePage():
        return "Home page"

def getAllEntry():
        headers = {
            'X-TrackerToken': "75497933ff68780e86ce333b790951b0"
            }
        response = Requests.request("GET", headers=headers)
        return response.text

def getspecificEntry():
        headers = {
            'X-TrackerToken': '75497933ff68780e86ce333b790951b0'
            }
        response = request.request("GET", headers=headers)
        return response.text
    
def addEntry():
        id = str(randint(5,100))
        payload = "{\"name\":\"Pytest Edit "+ id +"\"}"
        headers = {
            'X-TrackerToken': '75497933ff68780e86ce333b790951b0'
            }
        response = request.request("PUT", storyUrl, data=payload, headers=headers)
        return response.text


def modifyEntry():
        headers = {
            'X-TrackerToken': "75497933ff68780e86ce333b790951b0"
            }
        response = request.request("GET", headers=headers)
        return response.text


def deleteEntry():
        headers = {
            'X-TrackerToken': "75497933ff68780e86ce333b790951b0"
            }
        response = request.request("GET", headers=headers)
        return response.text        


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    app.run(host="0.0.0.0", port=8000)
