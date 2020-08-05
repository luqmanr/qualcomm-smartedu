import base64
from pathlib import Path
import os
from flask import Flask, request, Response
import jsonpickle
import json
from flask_cors import CORS
from dotenv import load_dotenv
import datetime
import cv2

app = Flask(__name__)
cors = CORS(app)
env_path = Path('.') / 'base64.env'
load_dotenv(dotenv_path=env_path)

api_port = os.getenv("BASE64_SERVICE_PORT")
video_stream = os.getenv("VIDEO_STREAM")

@app.route('/webcam_snapshot', methods = ['GET'])
def webcam_snapshot():
    print(video_stream)

    status = 200
    result = ""
    
    try:
        cap = cv2.VideoCapture(video_stream)
        retval, image = cap.read()
        retval, buffer = cv2.imencode('.jpg', image)
        base64_img = base64.b64encode(buffer)
        base64_img = base64_img.decode("utf-8")
        # print(base64_img.decode("utf-8"))
        cap.release()

        result = base64_img
    except:
        result = "Failed to capture webcam!"
        status = 500

    response = {
        "status": status,
        "return": result
    }

    response = jsonpickle.encode(response)
    return Response(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=api_port, threaded=True, debug=True)
