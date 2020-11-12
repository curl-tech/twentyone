from sklearn.metrics import *
from ..tasks.tasks import Task


class Evaluation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def evaluate_model(task: Task, y_pred=None, y_actual=None):
        if task.eval_metric == "accuracy":
            return accuracy_score(y_actual, y_pred)
