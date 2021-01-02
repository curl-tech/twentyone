import pickle
import sys

sys.path.append("..")

from tasks.tasks import Task
from .data_type import DataType
from .data_meta import DataMeta
from .load_lib import *

class Data:
    def __init__(self, data_settings) -> None:
        self.settings = data_settings
        self._id = None
        self.name = None
        self.meta: DataMeta = None
        self.data = None
        self.data_type: DataType = None

    @staticmethod
    def load_data_id(location, data_id):
        path = location + data_id + ".pickle"
        with open(path, "rb") as fp:
            data = pickle.load(fp)
        return data

    def save(self, data_id, data):
        location = self.settings["data_save_loc"]
        path = location + data_id + ".pickle"
        with open(path, "wb") as fp:
            pickle.dump(data, fp)    

    def clean(self):
        pass

    # Modify the data to a format which is suitable for the specific ML task
    def prepare(self):
        pass

    def modify(self):
        pass

    def append(self):
        pass

    def delete(self):
        pass

