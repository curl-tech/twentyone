import abc
from enum import Enum
from abc import abstractmethod

class Data(abc.ABC):
    def __init__(self) -> None:
        self.num_obs = None
        self.num_features = None
        self.size = None
        self.data = None
        self.type: DataType = None

    @abstractmethod
    def clean():
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
