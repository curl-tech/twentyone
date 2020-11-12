import abc
import pandas as pd
from abc import abstractmethod
from sklearn.model_selection import train_test_split

import sys
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
        self.obs = None
        self.target = None

        self.trainX = None
        self.trainY = None
        self.testX = None
        self.testY = None

        self.features_names = None
        self.target_names = None

        self.obs_type: DataType = None
        self.target_type = None

    # Load entire data or a batch, based on data size and type of task
    @staticmethod
    def load(config, task: Task):
        data = None
        if task.data_type == DataType.Tabular:
            data = TabularData(config)
            data.load_data()
        
        return data

    def clean():
        pass

    # Modify the data to a format which is suitable for the specific ML task
    def prepare():
        pass

    def modify():
        pass

    def append():
        pass

    def delete():
        pass

class TabularData(Data):
    def __init__(self, config) -> None:
        super().__init__(config)

    def load_data(self):
        source = self.config["data"]["source"]
        data_id = self.config["data"]["data_id"]
        if source == "sample":
            ld = eval("load_" + data_id + "()")
            obs = ld.data
            target = ld.target

            ld_df = pd.DataFrame(obs, columns=ld.feature_names)
            ld_df["target_"] = target

            if self.config["model"]["training"]["mode"] == "single_train_test":
                train_split = self.config["model"]["training"]["mode_details"]["train_split"] 
                train, test = train_test_split(ld_df, train_size=train_split)
                self.trainX  = train[ld.feature_names]
                self.trainY  = train["target_"]
                self.testX  = test[ld.feature_names]
                self.testY  = test["target_"]
