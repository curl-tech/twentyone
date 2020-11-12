import yaml
import sys

from sklearn.model_selection import train_test_split
from sklearn import metrics

sys.path.append("src")

from tasks.tasks import Task
from data.data import Data
from models.training import Trainer

if __name__ == "__main__":
    config_path = "config/config.yaml"

    with open(config_path, "r") as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)
    
    task = Task(config)
    data = Data.load(config, task)
    trainer = Trainer(config, data, task)

    best_res = trainer.train()
    print(best_res)
