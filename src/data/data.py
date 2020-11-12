import abc
from enum import Enum
from abc import abstractmethod

class Data(abc.ABC):
    def __init__(self, config) -> None:
        self.config = config
        self.num_obs = None
        self.num_features = None
        self.size = None
        self.obs = None
        self.target = None
        self.features_names = None
        self.target_names = None
        self.obs_type: DataType = None
        self.target_type = None

    # Load entire data or a batch, based on data size and type of task
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def clean():
        pass

    # Modify the data to a format which is suitable for the specific ML task
    @abstractmethod
    def prepare():
        pass

    @abstractmethod
    def modify():
        pass

    @abstractmethod
    def append():
        pass

    @abstractmethod
    def delete():
        pass

class DataType(Enum):
    # When you add a new data type, modify from_string method accordingly
    Image = 0
    Text = 1
    Tabular = 2
    Audio = 3
    Single_TS = 4    
    Multi_TS = 5   
    Location = 6
    Graph = 7

    @staticmethod
    def from_str(dt_str):
        l_dt_str = dt_str.to_lower()

        if l_dt_str == "image":
            return DataType.Image
        elif l_dt_str == "text":
            return DataType.Text
        elif l_dt_str == "audio":
            return DataType.Audio
        elif l_dt_str == "tabular":
            return DataType.Tabular
        elif l_dt_str == "single_ts":
            return DataType.Single_TS
        elif l_dt_str == "multi_ts":
            return DataType.Multi_TS
        elif l_dt_str == "location":
            return DataType.Location
        elif l_dt_str == "graph":
            return DataType.Graph
        else:
            return None

