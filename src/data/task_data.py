# This is what is used by models and it is not saved in the DB, 
# it is created every time the training starts.

from .data import Data

class TaskData:
    def __init__(self) -> None:
        self.trainX = None
        self.trainY = None
        self.valX = None
        self.valY = None
        self.testX = None
        self.testY = None

        self.data_type = None