#! /usr/bin/env python3

import os
import jsonpickle
import json

def response(request):
    payload = json.dumps(request.json)
    payload = json.loads(payload)
    user_image = payload["user_image"]
    client_id = payload["client_id"]

    if client_id == "test":
        user_id_rkb = "unregistered"
        confidence_level = 1.0000
        status = 0
        masker = "true"

        response = {"result":[{
            "user_id_rkb": user_id_rkb,
            "confidence_level": confidence_level,
            "status": status,
            "masker": masker
        }]}
    else:
        response = {
            "result":[
                # {"status" : 1}
                1,2,3,4,5,6,7
            ]
        }

    response = jsonpickle.encode(response)
    return response