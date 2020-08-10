import base64
from pathlib import Path
import os
from flask import Flask, request, Response, send_from_directory
import jsonpickle
import json, csv
from flask_cors import CORS
from dotenv import load_dotenv
import datetime
from tempfile import NamedTemporaryFile
import shutil
import csv
import time
import subprocess
import threading
import inspect
import ctypes

from services import register, login, verification
from exec_file import monitoring, autotrain
from utills import imageOps, faceOps

app = Flask(__name__)
cors = CORS(app)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_port = os.getenv("API_PORT")
file_storage = os.getenv("FILE_STORAGE")
image_storage = os.getenv("IMG_STORAGE")
cheating_storage = os.getenv("CHEATING_STORAGE")

tempfile = NamedTemporaryFile(mode='w', delete=False)

@app.route('/register_user', methods = ['POST'])
def register_user():

    payload = json.dumps(request.json)
    payload = json.loads(payload)

    email = payload["user_email"]
    image = payload["user_image"] 

    imagePath = image_storage + "/register" + "/" + email
    imageOps.decodeAndSaveImage(imagePath, image)

    csv_file = os.path.join(file_storage, "register.csv")

    # write data and wait 3 seconds reading database register.csv to get train_status
    response = register.WR_database(csv_file, payload)

    response = jsonpickle.encode(response)
    return Response(response)

@app.route('/login_service', methods = ['POST'])
def login_service():
    payload = json.dumps(request.json)
    payload = json.loads(payload)

    email = payload["user_email"]
    password = payload["user_password"]
    csvfilename = file_storage + "/register.csv"

    response = login.Read_DB(csvfilename, email, password)
    
    response = jsonpickle.encode(response)
    return Response(response)

@app.route('/face_verification', methods = ['POST'])
def face_verification():
    global main_analyze_threads
    global autotrain_threads

    main_analyze_threads = []

    payload = json.dumps(request.json)
    payload = json.loads(payload)

    image = payload["user_image"]
    email = payload["user_email"]

    csv_file = os.path.join(file_storage, "verification.csv")

    imagePath = image_storage + "/verification" + "/" + email
    imageOps.decodeAndSaveImage(imagePath, image)

    response = verification.write_read_DB(autotrain_threads, main_analyze_threads, csv_file, email)
    print(response)

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
        user_encoding = faceOps.generate_face_encoding(user_email, file_storage)
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
    return send_from_directory(cheating_storage, "cheating-detection.csv")

@app.route('/stop_monitoring', methods = ['POST'])
def stop_monitoring():

    monitoring.stop_monitoring(main_analyze_threads)
    autotrain.run_autotrain_thread(autotrain_threads)

    return "OK"

@app.errorhandler(404)
def not_found(error=None):

    response = {
        "status": 404,
        "message": "Not Found: " + request.url
    }

    response = jsonpickle.encode(response)
    return Response(response)

# ---------------------------------------------------
# All routes below unused, only for checking purpose
# ---------------------------------------------------

@app.route('/start_monitoring', methods = ['POST'])
def start_monitoring_force():

    # cheating-detection.csv di write ke awal mula
    cheating_log_csv = os.path.join(cheating_storage, "cheating-detection.csv")
    with open(cheating_log_csv, "w") as writefile:
        fieldnames = ['Timestamp', 'Label', 'Cheating Status']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)
        writer.writeheader()

    global main_analyze_threads
    main_analyze_threads = []

    payload = json.dumps(request.json)
    payload = json.loads(payload)

    email = payload["user_email"]

    monitoring.start_monitoring(main_analyze_threads, email)

    return "OK"

@app.route('/start_autotrain', methods = ['POST'])
def start_autotrain():

    autotrain.run_autotrain_thread(autotrain_threads)

    return "OK"

@app.route('/stop_autotrain', methods = ['POST'])
def stop_autotrain():

    autotrain.turn_autotrain_off(autotrain_threads)

    return "OK"

if __name__ == '__main__':
    main_analyze_threads = []
    autotrain_threads = []

    app.run(host='127.0.0.1', port=api_port, threaded=True, debug=True)
