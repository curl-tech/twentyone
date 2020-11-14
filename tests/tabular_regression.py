import yaml

import pandas as pd

import sys
sys.path.append("src")

from tasks.tasks import Task
from data.data import Data
from models.model import Model

if __name__ == "__main__":
    config_path = "config/config_energy.yaml"

    with open(config_path, "r") as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)
    
    d=None
    data_config = None

    data_path = "inputs/tabular/energy.xlsx"
    data_config_path = "inputs/tabular/energy.yaml"
    d = pd.read_excel(data_path, index_col="date")

    with open(data_config_path, "r") as fp:
        data_config = yaml.load(fp, Loader=yaml.FullLoader)
    
    task = Task(config)
    data = Data.load(config, task, d, data_config)
    #Data.save(config, data)
    model = Model(config, task, data)
    best_res = model.train(save_model=True)
    print(best_res)
    res = model.infer(task.id, data.testX[0])
    print(res)
