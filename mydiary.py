from flask import request,url_for
from flask_api import FlaskAPI,status,exceptions

app = FlaskAPI(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Homepage'


if __name__ == "__main__":
    app.run(debug=True)