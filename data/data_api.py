'''
test api curl command
$ curl -X POST http://localhost:3000/
'''

import base64
from pathlib import Path
import os
from flask import Flask, request, Response, send_from_directory
import jsonpickle
import json, csv
from flask_cors import CORS
from dotenv import load_dotenv
import datetime

app = Flask(__name__)
cors = CORS(app)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_port = os.getenv("API_PORT")
file_storage = os.getenv("FILE_STORAGE")

class RegistrationRequest:
    def __init__(self, user_email, user_name, user_password, user_image):
        self.email = user_email
        self.user_name = user_name
        self.user_password = user_password
        self.base64 - user_image

class VerificationRequest:
    def __init__(self, user_email, user_image):
        self.email = user_email
        self.base64 = user_image

@app.route('/register_user', methods = ['POST'])
def register_user():
    # print("New request from %s" % request.remote_addr)
    payload = json.dumps(request.json)
    payload = json.loads(payload)

    user_email = payload["user_email"]

    user_file = os.path.join(file_storage, (str(user_email) + ".json"))
    user_data = payload
    user_encoding = {"user_encoding":generate_face_encoding(user_email, file_storage)}

    user_data.update(user_encoding)

    result = "REGISTERED SUCCESSFULLY"
    status = 200

    if not os.path.exists(user_file):
        with open(user_file, 'w') as write_file:
        #     # write_file.write(user_data)
            json.dump(user_data, write_file)
    else:
        status = 500
        result = "USER EXISTS"

    print(user_data)

    response = {
        "status": status,
        "return": result
    }

    # print(response)
    response = jsonpickle.encode(response)
    return Response(response)

@app.route('/login_service', methods = ['POST'])
def login_service():
    payload = json.dumps(request.json)
    payload = json.loads(payload)

    user_email = payload["user_email"]
    user_password = payload["user_password"]

    user_file = os.path.join(file_storage, (str(user_email) + ".json"))
    try:
        with open(user_file) as json_file:
            user_data = json.load(json_file)

            if user_password == user_data["user_password"]:
                result = "Login Successfull"
                status = 200
            else:
                result = "Wrong email or password, please try again"
                status = 500
    except:
        result = "Wrong email or password, please try again"
        status = 500

    response = {
        "status": status,
        "return": result
    }
    response = jsonpickle.encode(response)
    return Response(response)

@app.route('/face_verification', methods = ['POST'])
def face_verification():
    payload = json.dumps(request.json)
    payload = json.loads(payload)

    user_email = payload["user_email"]
    user_file = os.path.join(file_storage, (str(user_email) + ".json"))

    result = ""
    status = 200

    if os.path.exists(user_file):
        with open(user_file) as json_file:
            user_data = json.load(json_file)
            user_name = user_data["user_name"]
            result = "Face Verified, welcome %s!" % user_name
    else:
        result = "Face not verified!"
        status = 500

    response = {
        "status": status,
        "return": result
    }

    # print(response)
    response = jsonpickle.encode(response)
    return Response(response)

@app.route('/delete_user', methods = ['POST'])
def delete_user():
    payload = json.dumps(request.json)
    payload = json.loads(payload)

    user_email = payload["user_email"]
    user_file = os.path.join(file_storage, (str(user_email) + ".json"))

    result = "user removed successfully"
    status = 200

    if os.path.exists(user_file):
        os.remove(user_file)
        user_encoding = generate_face_encoding(user_email, file_storage)
    else:
        status = 500
        result = "user doesn't exists"
    
    if os.path.exists(user_encoding):
        os.remove(user_encoding)
    else:
        status = 500
        result = "user doesn't exists"

    response = {
        "status": status,
        "return": result
    }

    # print(response)
    response = jsonpickle.encode(response)
    return Response(response)

@app.route('/cheating_log')
def cheating_log():
    # cheating_log_csv = os.path.join("/home/ubuntu/workspace/face-verification/result/result.csv")
    # print(cheating_log_csv)
    return send_from_directory("/home/ubuntu/workspace/face-verification/result", "result.csv")
 

def generate_face_encoding(email, file_storage):
    encoding_filename = os.path.join(file_storage, (email + ".npy"))
    user_data = "temp encoding"
    if not os.path.exists(encoding_filename):
        with open(encoding_filename, 'w') as write_file:
            write_file.write(user_data)
    else:
        pass

    return encoding_filename

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=api_port, threaded=True, debug=True)
