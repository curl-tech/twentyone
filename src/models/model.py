from sklearn import model_selection
import yaml
import numpy as np
from itertools import product
import pickle
import os
from tqdm import tqdm

import sys
sys.path.append("..")

from .load_lib import *
from .train_results import TrainResults
from tasks.tasks import Task, TaskType
from data.data import Data, DataType
from utils import model_utils as mu

from .evaluation import Evaluation

class Model:

    def __init__(self, config=None, task: Task=None, data: Data=None, pipeline=None) -> None:
        self.config = config
        self.data = data
        self.task = task
        self.pipeline = pipeline
        self.best_model = []

    def train(self, save_model=True):
        data_type = DataType.from_str(self.config["task"]["data_details"]["type"])
        candidates = get_candidate_models(self.config, self.task.type, data_type)
        n_best = self.config["model"]["training"]["model_selection"]["n_best"]
        save_mode = self.config["model"]["training"]["save_mode"]
                
        cand_scores = []
        for c in tqdm(candidates):
            model_hypers = get_model_hypers(c)
            for mh in model_hypers:
                model_str = c["name"] + "(" + ", ".join(mh) + ")"
                model = eval(model_str)
                score = []
                for i in range(len(self.data.trainX)):
                    model.fit(self.data.trainX[i], self.data.trainY[i])
                    prediction = model.predict(self.data.testX[i])
                    score.append(Evaluation.evaluate_model(self.task, prediction, self.data.testY[i]))
                avg_score = np.mean(score)
                cand_scores.append({"name": c["name"], "hyper":mh, "score": avg_score})

        cand_sort = sorted(cand_scores,  key=lambda x: x["score"], reverse=True)

        if len(cand_sort) >= n_best:
            best_candidates = cand_sort[0:n_best]
        else:
            best_candidates = cand_sort
        
        models = self.get_models(best_candidates, mode=save_mode)
        len_train = len(self.data.trainX) if save_mode=="all_train" else 1
        train_results = TrainResults(self.config, best_candidates, models, len_train, len(cand_scores))
        if save_model:
            self.save_models(train_results)
        return train_results

    def get_models(self, best_candidates, mode="last_train"):
        models = []
        for candidates in best_candidates:
            model_str = candidates["name"] + "(" + ", ".join(candidates["hyper"]) + ")"
            model = eval(model_str)
            model_ = []
            if mode == "all_train":
                for i in range(len(self.data.trainX)):
                    model.fit(self.data.trainX[i], self.data.trainY[i])
                    model_.append(model)
            elif mode == "last_train":
                model.fit(self.data.trainX[-1], self.data.trainY[-1])
                model_.append(model)
            elif mode == "first_train":
                model.fit(self.data.trainX[0], self.data.trainY[0])
                model_.append(model)
            models.append(model_)
        return models
    
    def save_models(self, train_results):
        file_name = self.config["task"]["_id"] + ".pickle"
        folder_name = self.config["model"]["save_location"]
        path = folder_name + file_name

        with open(path, "wb") as fp:
            pickle.dump(train_results, fp)
    
    @staticmethod
    def load_models(location, task_id):
        file_name = task_id + ".pickle"
        folder_name = location
        path = folder_name + file_name

        if os.path.exists(path):
            with open(path, "rb") as fp:
                res = pickle.load(fp)
            return res
        else:
            return None
    
    # Not finished
    def infer(self, model_loc, task_id, data=None):
        tr = Model.load_models(model_loc, task_id)
        models = tr.models
        res = []
        mode = self.config["model"]["inference"]["mode"]
        if mode == "single_model":
            model = models[0]
            res = [model[0].predict(data)]
        elif mode == "ensemble":
            for model in models:
                res.append(model[0].predict(data))
        return res

def get_candidate_models(config, task_type, data_type, get_best=None):
    models_path = config["model"]["model_db"]
    with open(models_path, "r") as fp:
        all_models = yaml.load(fp, Loader=yaml.FullLoader)
    candidates = [x for x in all_models if TaskType.from_str(x["type"]) == task_type and DataType.from_str(x["data_type"]) == data_type]
    if get_best is not None:
        candidates = filter_best_candidates(config, candidates)
    return candidates

def get_models(train_res):
    pass

# for future implementation, faster model selection using past experience
def filter_best_candidates(config, candidates):
    pass

# get all combinations of hyper parameters
def get_model_hypers(candidate):
    hypers = []
    for ch in candidate["hyper"]:
        hyper = []
        if ch["vary"]:
            if ch["type"] == "option":
                for opt in ch["options"]:
                    hyper.append(ch["name"] + "='" + str(opt)+"'")
            elif ch["type"] == "bool":
                hyper.append(ch["name"] + "=True")
                hyper.append(ch["name"] + "=False")
            elif ch["type"] == "number":
                min_r = ch["range"]["min"]
                max_r = ch["range"]["max"]
                num_samp = ch["range"]["num_samp"]
                r_type = ch["range"]["type"]
                if r_type == "linear":
                    for r in np.linspace(min_r, max_r, num=num_samp):
                        hyper.append(ch["name"] + "=" + str(r))
                elif r_type == "log":
                    for r in np.logspace(np.log10(min_r), np.log10(max_r), num=num_samp):
                        hyper.append(ch["name"] + "=" + str(r))
        else:
            if ch["type"] == "option":
                hyper.append(ch["name"] + "='" + str(ch["default"]) + "'")
            else:
                hyper.append(ch["name"] + "=" + str(ch["default"]))
        
        hypers.append(hyper)
    
    model_hypers = product(*hypers)
    return model_hypers