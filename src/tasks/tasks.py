# Class definition for the tasks
from enum import Enum

import sys
sys.path.append("..")

from data.data_type import DataType

class Task:
    def __init__(self, config) -> None:
        self.config = config
        self.type: TaskType = None
        self.data_type: DataType = None
        self.eval_metric = None

        if "task" in config:
            self.type = TaskType.from_str(config["task"]["type"])
            self.data_type = DataType.from_str(config["task"]["data_details"]["type"])
            self.eval_metric = config["task"]["evaluation"]["metric"]

    def map_task_pipeline():
        pass

    def execute_task():
        pass

class TaskType(Enum):
    Classification = 1
    Regression = 2
    Clustering = 3
    Forecasting = 4
    AnomalyDetection = 5
    RegionDetection = 6
    Tagging = 7
    SeqSeq = 8

    @staticmethod
    def from_str(tt_str):
        l_str = tt_str.lower()

        if l_str == "classification":
            return TaskType.Classification
        elif l_str == "regression":
            return TaskType.Regression
        elif l_str == "clustering":
            return TaskType.Clustering
        elif l_str == "forecasting":
            return TaskType.Forecasting
        elif l_str == "anomaly_detection":
            return TaskType.AnomalyDetection
        elif l_str == "region_detection":
            return TaskType.RegionDetection
        elif l_str == "tagging":
            return TaskType.Tagging
        elif l_str == "graph":
            return DataType.Graph
        else:
            return None
