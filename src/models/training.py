import yaml
import numpy as np
from itertools import combinations, product

from .load_lib import *
from ..tasks.tasks import Task, TaskType
from ..data.data import Data, DataType
from ..utils import model_utils as mu

from .evaluation import Evaluation

class Trainer:
    def __init__(self, config, data: Data, task: Task, pipeline) -> None:
        self.config = config
        self.data = data
        self.task = task
        self.pipeline = pipeline
        self.best_model = []

    def train(self):
        data_type = DataType.from_str(self.config["task"]["data_details"]["type"])
        candidates = get_candidate_models(self.config, self.task.type, data_type)
        need_ensemble = self.config["model"]["traning"]["need_ensemble"]

        cand_scores = {}
        for c in candidates:
            model_hypers = get_model_hypers(c)
            for mh in model_hypers:
                model_str = c["name"] + "(" + ", ".join(mh) + ")"
                model = eval(model_str)
                if self.config["training"]["mode"] == "single_train_test":
                    model.fit(self.data.train_X, self.data.train_y)
                    prediction = model.predict(self.data.test_X)
                    score = Evaluation.evaluate_model(self.task, prediction, self.data.test_y)
                    cand_scores[model_str] = score

        n_best = 1
        if need_ensemble:
            n_best = self.config["model"]["traning"]["ensemble_properties"]["n_best"]
        
        cand_sort = sorted(cand_scores.items(),  key=lambda x: x[1], reverse=True)[n_best]

        return cand_sort

def get_candidate_models(config, task_type, data_type, get_best=None):
    models_path = config["model"]["model_db"]
    with open(models_path, "r") as fp:
        all_models = yaml.load(fp)
    candidates = [x for x in all_models if TaskType.from_str(x["type"]) == task_type and DataType.from_str(x["data_type"]) == data_type]
    if get_best is not None:
        candidates = filter_best_candidates(config, candidates)
    return candidates

# for future implementation, faster model development using past experience
def filter_best_candidates(config, candidates):
    pass

# 
def get_model_hypers(candidate):
    hypers = []
    model_str = candidate["name"]
    for ch in candidate["hyper"]:
        hyper = []
        if ch["vary"]:
            if ch["type"] == "option":
                for opt in ch["options"]:
                    hyper.append(ch["name"] + "=" + opt)
            elif ch["type"] == "bool":
                hyper.append(ch["name"] + "=true")
                hyper.append(ch["name"] + "=false")
            elif ch["type"] == "range":
                min_r = ch["range"]["min"]
                max_r = ch["range"]["max"]
                num_samp = ch["range"]["num_samp"]
                r_type = ch["range"]["type"]
                if r_type == "linear":
                    for r in np.linspace(min_r, max_r, num=num_samp):
                        hyper.append(ch["name"] + "=" + str(r))
                elif r_type == "log":
                    for r in np.logspace(min_r, max_r, num=num_samp):
                        hyper.append(ch["name"] + "=" + str(r))
        else:
            hyper.append(ch["name"] + "=" + ch["default"])
        hypers.append(hyper)
    
    model_hypers = product(*hypers)

    return model_hypers