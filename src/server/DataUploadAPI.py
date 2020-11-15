from flask import Blueprint
import yaml
import json
import sys
sys.path.append("..")

from data.data import Data

data_upload_api = Blueprint('data_upload_api', __name__)

config_path = "config/config_energy.yaml"
with open(config_path, "r") as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)

@data_upload_api.route("/data_upload")
def data_upload():
    # data_path = "inputs/tabular/energy.xlsx"
    # data_config_path = "inputs/tabular/energy.yaml"
    # d = pd.read_excel(data_path, index_col="date")

    # with open(data_config_path, "r") as fp:
    # data_config = yaml.load(fp, Loader=yaml.FullLoader)
    location = config["data"]["save_location"]

    data = Data.load_api(file_data, data_config)
    # generate a data_id
    Data.save(location, data_id, data)

    return "Data Upload!"


from flask import Blueprint, request, jsonify
from base64 import b64decode, b64encode

import pandas as pd
import json
import os
import base64

import random
import string

# from data.data import Data

data_upload_api = Blueprint('data_upload_api', __name__)

@data_upload_api.route("/data_upload", methods = ['POST'])
def data_upload():
    request_method = request.method

    if request_method == "POST":
        file = request.files['file']
        foo=file.filename
        print("File Name : ", foo)
        unparsedFile = file.read()
        dframe = pd.read_excel(file)
        data_config = jsonify(request.data)
        file_data = unparsedFile
        print("Unparsed File Excel : ", unparsedFile)
        print("Dframe : ", dframe)
        print("Request Data : ", jsonify(request.data))
        location = data_config["data"]["save_location"]
        print("Location", location)

        letters_and_digits = string.ascii_letters + string.digits
        data_id = ''.join((random.choice(letters_and_digits) for i in range(8)))
        print("Data ID is:", data_id)

        # Data.save(location, data_id, file_data)

    return "Data Upload Response"
