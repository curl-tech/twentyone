import abc
import copy
import pickle
import pandas as pd
from abc import abstractmethod
from sklearn.model_selection import train_test_split

import sys

from sklearn.utils import shuffle
sys.path.append("..")

from tasks.tasks import Task
from .data_type import DataType
from .load_lib import *

class Data:
    def __init__(self, config) -> None:
        self.config = config
        self.num_obs = None
        self.num_features = None
        self.size = None
        self.data = None
        self.target = None

        self.trainX = None
        self.trainY = None
        self.testX = None
        self.testY = None

        self.features_names = None
        self.target_names = None

        self.obs_type: DataType = None
        self.target_type = None

    @staticmethod
    def save_api(data_=None, data_config=None):
        if data_config.data_type.lower() == "tabular":
            data = TabularData()
            data.load_data("file_sent", data_, data_config)
        elif data_config.data_type.lower() == "image":
            data = ImageData()
            data.load_data("file_sent", data_, data_config)

    @staticmethod
    def load_data_id(location, data_id):
        path = location + data_id + ".pickle"
        with open(path, "rb") as fp:
            data = pickle.load(fp)
        return data

    # Load entire data or a batch, based on data size and type of task
    @staticmethod
    def load(config, task: Task, data_=None, data_config=None):
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
    
    @staticmethod
    def save(location, data_id, data):
        # file_name = config["task"]["data_details"]["data_id"] + ".pickle"
        # folder_name = config["data"]["save_location"]
        path = location + data_id + ".pickle"
        with open(path, "wb") as fp:
            pickle.dump(data, fp)

    def clean(self):
        remove_na_rows = self.config["data"]["cleaning"]["properties"]["remove_rows"]
        remove_na_cols = self.config["data"]["cleaning"]["properties"]["remove_cols"]
        if remove_na_rows:
            self.data.dropna(axis=0, inplace=True)
        if remove_na_cols:
            self.data.dropna(axis=1, inplace=True)

    # Modify the data to a format which is suitable for the specific ML task
    def prepare(self):
        pass

    def modify(self):
        pass

    def append(self):
        pass

    def delete(self):
        pass

class TabularData(Data):
    def __init__(self, config=None) -> None:
        super().__init__(config)

    # Can't use in algo trading yet!!!
    def load_data(self, source, data=None, data_config=None):
        if source == "sample":
            data_id = self.config["task"]["data_id"]
            ld = eval("load_" + data_id + "()")
            obs = ld.data
            target = ld.target
            ld_df = pd.DataFrame(obs, columns=ld.feature_names)

            self.data = ld_df
            self.target = target
            self.features_names = ld.feature_names
            self.data["target_"] = self.target
            self.clean()
            self.create_train_test()
        if source == "file_sent": 
            self.data = copy.deepcopy(data)
            if data_config["target"] is None:
                if data_config["compute_target"] is not None:
                    feat = data_config["compute_target"]["feature"]
                    mode = data_config["compute_target"]["mode"]
                    num_sample = data_config["compute_target"]["num1"]
                    if mode == "lead_lag":
                        self.target = data[feat].shift(num_sample)
            else:
                self.target = data[data_config["target"]]
                self.data.drop([data_config["target"]], axis='columns', inplace=True)

            remove_cols = data_config["remove_cols"]
            self.data.drop(remove_cols, axis='columns', inplace=True)

            self.features_names = self.data.columns  
            self.data["target_"] = self.target
            
            self.clean()
            self.create_train_test()
    
    def create_train_test(self):
        mode = self.config["model"]["training"]["mode"]
        shuffle = self.config["model"]["training"]["random_order"]
        if mode == "single_train_test":
            train_split = self.config["model"]["training"]["mode_details"]["train_split"] 
            train, test = train_test_split(self.data, train_size=train_split, shuffle=shuffle)
            self.trainX  = [train[self.features_names]]
            self.trainY  = [train["target_"]]
            self.testX  = [test[self.features_names]]
            self.testY  = [test["target_"]]
        # elif mode == "walk_forward":
        #     self.trainX, self.trainY, self.testX, self.testY = walk_fwd_split()

class ImageData(Data):
    def __init__(self, config) -> None:
        super().__init__(config)

    def load_data(self, data=None, data_config=None):
        self.create_train_test()
    
    def create_train_test(self):
        pass