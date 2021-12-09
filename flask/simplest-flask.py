from flask import Flask
from flask import request


app = Flask(__name__)
my_dict = dict()


@app.route("/<element_id>", methods=['GET'])
def get(element_id):
    print(f'getting value for element: {element_id} {type(element_id)}')
    return my_dict.get(element_id)


# Use when you want to add a new entity
@app.route("/add", methods=['POST'])
def add():
    print('I am in divide')
    payload = request.json
    payload_id_ = payload["id"]
    if payload_id_ not in my_dict:
        my_dict[payload_id_] = payload
    return my_dict


@app.route("/update", methods=['PUT'])
def update():
    payload = request.json
    my_dict[payload["id"]] = payload
    return my_dict


@app.route("/delete/<element_id>", methods=['DELETE'])
def delete(element_id):
    my_dict.pop(element_id)
    return my_dict


app.run(port=5001, debug=True)
