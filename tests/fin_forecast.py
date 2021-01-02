import yaml
import pandas as pd

import sys
sys.path.append("src")

from tasks.tasks import Task
from data.data import Data
from models.model import Model

if __name__ == "__main__":
    config_path = "config/config_fin.yaml"

    with open(config_path, "r") as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)

    
