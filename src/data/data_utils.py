import pickle

from .data_type import DataType
from .tabular_data import TabularData
from .image_data import ImageData


def load(config, task, data_=None, data_config=None):
    data = None
    source = config["task"]["data_details"]["source"]
    if source == "local_db":
        file_name = config["task"]["data_id"] + ".pickle"
        load_path = config["data"]["save_location"] + file_name
        with open(load_path, "rb") as fp:
            data = pickle.load(fp)
    else:
        source = config["task"]["data_details"]["source"]
        if task.data_type == DataType.Tabular:
            data = TabularData(config)
            data.load_data(source, data_, data_config)
        elif task.data_type == DataType.Image:
            data = ImageData(config)
            data.load_data(source, data_, data_config)
    return data

def save_api(data_=None, data_config=None):
    if data_config.data_type.lower() == "tabular":
        data = TabularData()
        data.load_data("file_sent", data_, data_config)
    elif data_config.data_type.lower() == "image":
        data = ImageData()
        data.load_data("file_sent", data_, data_config)

