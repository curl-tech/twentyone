import yaml
from flask import Blueprint

import sys
sys.path.append("..")

from tasks.tasks import Task
from data.data import Data
from models.model import Model

config_path = "config/config_energy.yaml"

with open(config_path, "r") as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)

new_task_api = Blueprint('new_task_api', __name__)

@new_task_api.route("/new_task")
def new_task():
    # Extract the Json string and convert it into an object
    # generate unique id, and add to the task object with key "_id"

    # replace the task element of config with task object
    config["task"] = "task_object"

    task = Task(config)
    data = Data.load_direct(config["data"]["save_location"], config["task"]["data_id"])
    model = Model(config, task, data)
    best_res = model.train(save_model=True)

    return str(best_res)