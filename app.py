from flask import Flask, request, render_template, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello"

@app.route('/something', methods=['GET'])
def something():
    return "Something"

if __name__ == '__main__':
    app.run(debug=True)