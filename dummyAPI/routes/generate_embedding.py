import os, csv
import numpy as np
import pandas as pd
import jsonpickle
import json

def response(request):
    embedding_array = np.arange(0,512.0001)
    # print('original array=', type(embedding_array))
    # 512_array = np.append(512_array, "luqmanr")

    # array_df = pd.DataFrame(columns=embedding_array)

    array_list = embedding_array.tolist()
    # array_list = [1.23235234,44.345345,4634634534.0456,123123.23123]

    print(type(array_list[0]))

    response = {
        "status": 0,
        "embedding" : array_list
    }

    response = jsonpickle.encode(response)
    return response