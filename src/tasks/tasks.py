# Class definition for the tasks
from enum import Enum

class Task:
    def __init__(self) -> None:
        self.type: TaskType = None

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
