import pandas as pd
import copy
from sklearn.model_selection import train_test_split

from .data import Data

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
    
    def clean(self, remove_na_rows, remove_na_cols):
        if remove_na_rows:
            self.data.dropna(axis=0, inplace=True)
        if remove_na_cols:
            self.data.dropna(axis=1, inplace=True)
