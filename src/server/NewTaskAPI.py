import yaml
from flask import Blueprint, request, jsonify
from base64 import b64decode, b64encode

import sys
import string
import random
sys.path.append("..")

from tasks.tasks import Task
from data.data import Data
from models.model import Model

config_path = "config/config.yaml"

with open(config_path, "r") as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)

new_task_api = Blueprint('new_task_api', __name__)

@new_task_api.route("/new_task", methods = ['POST'])
def new_task():
    request_method = request.method

    if request_method == "POST":
        # Extract the Json string and convert it into an object
        # generate unique id, and add to the task object with key "_id"

        # replace the task element of config with task object
        letters_and_digits = string.ascii_letters + string.digits
        _id = ''.join((random.choice(letters_and_digits) for i in range(8)))
        print("Unique ID is:", _id)
        print(request.get_json())
        task_object = request.get_json()
        task_object["task_object"]["_id"] = _id

        config["task"] = task_object["task_object"]

        task = Task(config)
        data = Data.load_data_id(config["data"]["save_location"], config["task"]["data_id"])
        model = Model(config, task, data)
        best_res = model.train(save_model=True)
        response = {}
        response["best_res"]=str(best_res)
        response["_id"] = _id

    return response