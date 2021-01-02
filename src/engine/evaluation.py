import sys
import numpy as np
from sklearn.metrics import *

sys.path.append("..")
from tasks.tasks import Task

sign_map = {"accuracy": 1, "mse": -1, "mape": -1, "f1": 1, "precision": 1, "recall": 1, "iou": 1, "cross_entropy": -1, "ap": 1, "bleu": 1}

class Evaluation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def evaluate_model(task: Task, y_pred=None, y_actual=None):
        metric = task.eval_metric
        sign = sign_map[metric]
        if metric == "accuracy":
            return sign * accuracy_score(y_actual, y_pred)
        elif metric == "mse":
            return sign * mean_squared_error(y_actual, y_pred)
