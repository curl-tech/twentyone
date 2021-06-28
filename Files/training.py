import yaml
from yaml.loader import FullLoader
import numpy as np
import pandas as pd
import json
import pandas as pd
from .libraries import *
import yaml
from yaml.loader import FullLoader
from Files.hyperparameter import hyperparameter as hp


    #pred=clf.predict(data)
    #print(roc_auc_score(y,pred))


class training:

    def train(userinputconfig,modelconfig,xdata,ydata):


        #b={"modeltype ":"classification", "modelname":"Logistic Regression","parameter":[{, "lr":73,"ishyper":True},{"modeltype":"classification", "modelname":"knn", "n_neighbours":3,"ishyper":"True"},{"modeltype ":"classification", "modelname":"decision trees", "ishyper":False}]}


        with open(modelconfig) as f:
            modelconfig= yaml.load(f,Loader=FullLoader)

        with open(userinputconfig) as file:
            userinputconfig=yaml.load(file,Loader=FullLoader)
        models=[]
        ans=[]
        for model in userinputconfig:
            if model["isSelected"]:
                hypers=[]
                keylist=[]
                for feature in model["hyper"]:
                    if feature["ischanged"]:
                        keylist.append(feature["name"])
                        hypers.append(feature["name"]+"="+ str(feature["value"]))
                model_str=model["modelname"] + "(" + ", ".join(hypers) + ")"
    
                hp.optimize(model_str,model["modelname"],userinputconfig)
