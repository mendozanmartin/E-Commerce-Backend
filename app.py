from flask import Flask, request, render_template, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/', methods=['GET'])
def landing():
    return "This is the back-end for our E-Commerce Website"

@app.route('/hello_world', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        json = request.get_json()
        body = int(json['string']) + 5
        return str(body)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")