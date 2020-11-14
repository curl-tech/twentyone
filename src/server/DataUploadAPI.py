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