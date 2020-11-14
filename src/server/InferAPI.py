import yaml
from flask import Blueprint

import sys
sys.path.append("..")

from tasks.tasks import Task
from data.data import Data
from models.model import Model

infer_api = Blueprint('infer_api', __name__)

config_path = "config/config.yaml"
with open(config_path, "r") as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)

@infer_api.route("/infer")
def infer():
    # in the response you get task id and data, convert data to right format
    model = Model()
    location = config["model"]["save_location"]
    res = model.infer(location, "task.id", "data")
    return res