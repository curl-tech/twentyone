from numpy.lib.shape_base import tile
import yaml
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append("src")

from tasks.tasks import Task
from data.data import Data
from engine.engine import Engine

if __name__ == "__main__":
    config_path = "config/config_energy.yaml"

    with open(config_path, "r") as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)
    
    d=None
    data_config = None
    
    task = Task(config)
    data = Data.load(config, task, d, data_config)
    #Data.save(config, data)

    model = Engine(config, task, data)
    best_res = model.train(save_model=True)
    print(best_res)

    res = model.infer(config["model"]["save_location"], task.id, data.testX[0])
    data.testX[0].to_excel("energy_test.xlsx")

    # plot
    ds = data.testY[0]
    res_df = pd.DataFrame(res[0], columns=["predicted"], index=ds.index)
    res_df["Actual"] = ds
    res_df.plot(title="Runs =" + str(best_res.num_runs))
    plt.show()
