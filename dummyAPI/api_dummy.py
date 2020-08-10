'''
test api curl command
$ curl -X POST http://localhost:3000/
'''

import base64
from PIL import Image
import cv2
from io import StringIO
import numpy as np
import os
from flask import Flask, request, Response
import jsonpickle
import json
from flask_cors import CORS

# from routes import generate_embedding
# from routes import inferencing_image
# from routes import register_image

app = Flask(__name__)
cors = CORS(app)
api_port = 3001

# @app.route('/InferencingImage', methods = ['POST'])
# def InferencingImage():
#     response = inferencing_image.response(request)
#     print(response)
#     return Response(response)

# @app.route('/RegisterImage', methods = ['POST'])
# def RegisterImage():
#     response = register_image.response(request)
#     print(response)
#     return Response(response)

# @app.route('/GenerateEmbedding', methods = ['POST'])
# def GenerateEmbedding():
#     response = generate_embedding.response(request)
#     print(response)
#     return Response(response)

# @app.route('/DecodeBase64', methods = ['POST'])
# def DecodeBase64():
#     # print(request)
#     payload = json.dumps(request.json)
#     payload = json.loads(payload)
#     print(payload)
#     response = {
#         "result": "SUCCESS"
#     }
#     print(response)
#     response = jsonpickle.encode(response)
#     return Response(response)

@app.route('/Success', methods = ['POST'])
def Success():
    # print(request)
    payload = json.dumps(request.json)
    payload = json.loads(payload)
    print(payload)
    response = {
        "status": 200,
        "result": "SUCCESS"
    }
    print(response)
    response = jsonpickle.encode(response)
    return Response(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=api_port, threaded=True, debug=True)

# with open("data.json", 'r') as read_file:
#     data = json.load(read_file)

# data["data"].append({"user_image" : user_image, "client_id" : client_id})
# with open("data.json", 'w') as write_file:
#     json.dump(data, write_file)