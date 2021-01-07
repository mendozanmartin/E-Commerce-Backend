from flask import Flask, request, render_template, url_for
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__, template_folder='templates')
CORS(app)

items = [
    {
        'title': 'Denim Jeans',
        'price': 29.99,
        'image': "https://www.blackdiamondequipment.com/on/demandware.static/-/Sites-bdel/default/dw0f24a23b/products/S19_Product_Images/S19_Apparel/750020_4010_FORGEDDENIM_MFORGEDDENIMPANTS.jpg",
        'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisl eros, pulvinar facilisis justo mollis, auctor consequat urna. Morbi a bibendum metus. Donec scelerisque sollicitudin enim eu venenatis. Duis tincidunt laoreet ex, in pretium orci vestibulum eget."
    },
    {
        'title': 'Polo shirt',
        'price': 19.99,
        'image': "https://www.prada.com/content/dam/pradanux_products/U/UJN/UJN444/1C61F0ZON/UJN444_1C61_F0ZON_S_181_SLF.png",
        'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisl eros, pulvinar facilisis justo mollis, auctor consequat urna. Morbi a bibendum metus. Donec scelerisque sollicitudin enim eu venenatis. Duis tincidunt laoreet ex, in pretium orci vestibulum eget."
    }
]

@app.route('/', methods=['GET'])
def landing():
    return "This is the back-end for our E-Commerce Website"

@app.route('/hello-world', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        json = request.get_json()
        body = int(json['string']) + 5
        return str(body)

@app.route('/get-items', methods=['GET'])
def get_items():
    global items
    if request.method == 'GET':
        json_object = json.dumps(items, indent = 4)
        return str(json_object)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

