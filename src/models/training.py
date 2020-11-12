import numpy as np

from .load_lib import *
from ..tasks.tasks import Task, TaskType
from ..data.data import Data, DataType

class Trainer:
    def __init__(self, config, data: Data, task: Task, pipeline) -> None:
        self.config = config
        self.data = data
        self.task = task
        self.pipeline = pipeline
        self.best_model = []

    def train(self):
        data_type = self.config["task"]["data_details"]["type"]
        if self.task.type == TaskType.Classification:
            pass
