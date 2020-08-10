#! /usr/bin/env python3

import os
import jsonpickle
import json

def response(request):
    payload = json.dumps(request.json)
    payload = json.loads(payload)
    print(payload)
    user_image = payload["user_image"]
    client_id = payload["client_id"]

    if client_id == "test":
        user_id_rkb = "unregistered"
        confidence_level = 1.0000
        status = 0
        masker = "true"

        response = {
            "status" : status, 
            "user_id_rkb" : user_id_rkb
        }
    else:
        response = {
            "status" : 5
        }

    response = jsonpickle.encode(response)
    return response