import yaml
from yaml.loader import FullLoader
import numpy as np
import pandas as pd
import json
import pandas as pd
from .libraries import *

def optimize(model_str,keylist,name,config):
    """
    This function in takes the string consisting of the name and the hyperparameters of the model and uses eval function to create the model.
    Keylist is the dictionary consisting of the infomation about the user input ('subject to further changes')
    Name is the name of the model selected (subject to future changes)
    """
    with open("config/model.yaml") as f:
        model_uni= yaml.load(f,Loader=FullLoader)

    with open("config/config.yaml") as new:
        config= yaml.load(new,Loader=FullLoader)

    x=pd.read_csv(config["xdata"])
    y=pd.read_csv(config["ydata"])

    params={}
    for i in model_uni:
        if i["name"]==name:
            for hyper in i["hyper"]:
                print(hyper)
                if hyper["name"] not in keylist:
                    if hyper["vary"]:
                        if hyper["type"]=="options":
                            params[hyper["name"]]=hyper["options"]
                        elif hyper["type"]=="bool":
                            params[hyper["name"]]=[True,False]
                        elif hyper["type"]=="float" or hyper["type"]=="int":
                            if hyper["range"]["type"]=="linear":
                                if hyper["type"]=="int":
                                    params[hyper["name"]]=(np.linspace(hyper["range"]["min"],hyper["range"]["max"],hyper["range"]["num_samp"])).astype(int)
                                else:
                                    params[hyper["name"]]=np.linspace(hyper["range"]["min"],hyper["range"]["max"],hyper["range"]["num_samp"])
                            if hyper["range"]["type"]=="log":
                                if hyper["type"]=="int":
                                    params[hyper["name"]]=(np.logspace(hyper["range"]["min"],hyper["range"]["max"],hyper["range"]["num_samp"])).astype(int)
                                else:
                                    params[hyper["name"]]=(np.logspace(hyper["range"]["min"],hyper["range"]["max"],hyper["range"]["num_samp"]))
                    else:
                        if hyper["type"]=="option":
                            params[hyper["name"]]=hyper["options"]
    model=eval(model_str)
    clf=RandomizedSearchCV(model, params,verbose=10)
    search=clf.fit(x,y)