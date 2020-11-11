import abc
from enum import Enum
from abc import abstractmethod

class Data(abc.ABC):
    def __init__(self) -> None:
        self.num_obs = None
        self.num_features = None
        self.size = None
        self.obs = None
        self.target = None
        self.features_names = None
        self.target_names = None
        self.obs_type: DataType = None
        self.target_type = None

    @abstractmethod
    def clean():
        pass

    # Modify the data to a format which is suitable for the specific ML task
    @abstractmethod
    def convert_to_standard():
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

    @abstractmethod
    def get_next_obs():
        pass

class DataType(Enum):
    Image = 0
    Text = 1
    Tabular = 2
    Audio = 3
    Single_TS = 4    
    Multi_TS = 5   
    Location = 6
    Graph = 7
