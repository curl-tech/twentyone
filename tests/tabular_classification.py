import yaml

import sys
sys.path.append("src")

from tasks.tasks import Task
from data.data import Data
from models.model import Model

if __name__ == "__main__":
    config_path = "config/config_iris.yaml"

    with open(config_path, "r") as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)
    
    task = Task(config)
    data = Data.load(config, task)
    model = Model(config, task, data)
    best_res = model.train(save_model=True)
    print(best_res)
    res = model.infer(task.id, data.testX[0])
    print(res)
