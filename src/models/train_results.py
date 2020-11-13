import pickle

class TrainResults:
    def __init__(self, config, best_models, models, len_train, num_runs=None) -> None:
        self.config = config
        self.best_models = best_models
        self.models = models
        self.len_train = len_train
        self.num_runs = num_runs
    
    def __str__(self):
        model_str = []
        for bm in self.best_models:
            model_str.append(bm["name"] + "(" + ", ".join(bm["hyper"]) + "), score = " + str(bm["score"]))
        ret = "Runs = " + str(self.num_runs) + "\n" + str(model_str)
        return ret