import yaml
from yaml.loader import FullLoader
import numpy as np
import pandas as pd
import json
import pandas as pd
from .libraries import *
import yaml
from yaml.loader import FullLoader
from .hyperparameter import *


    #pred=clf.predict(data)
    #print(roc_auc_score(y,pred))


class training:

    def train(userconfig,config,xdata,ydata):

        b={"models":[{"modeltype":"regression","modelname":"DecisionTreeClassifier","ishyper":True,"hyper":{"criterion":"'gini'"}},{"modeltype":"classification","modelname":"KNeighborsClassifier","ishyper":True,"hyper":{"n_neighbors":5,"leaf_size":30}}]}
        x=json.dumps(b)
        parameters=json.loads(x)
        #b={"modeltype ":"classification", "modelname":"Logistic Regression","parameter":[{, "lr":73,"ishyper":True},{"modeltype":"classification", "modelname":"knn", "n_neighbours":3,"ishyper":"True"},{"modeltype ":"classification", "modelname":"decision trees", "ishyper":False}]}


        with open("config/model.yaml") as f:
            model_uni= yaml.load(f,Loader=FullLoader)

        models=[]
        ans=[]
        for i in parameters['models']:
            hypers=[]
            keylist=[]
            if i["ishyper"]:
                for key,val in i["hyper"].items():
                    keylist.append(key)
                    hypers.append(key+"="+str(val))
                model_str=i["modelname"] + "(" + ", ".join(hypers) + ")"
                print(model_str)
                optimize(model_str,keylist,i["modelname"],config)
