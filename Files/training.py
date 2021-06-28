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


        


        with open(modelconfig) as f:
            modelconfig= yaml.load(f,Loader=FullLoader) #has info about where the data is stored and where the model must be stored

        with open(userinputconfig) as file:
            userinputconfig=yaml.load(file,Loader=FullLoader)
        models=[]
        ans=[]
        
        for model in userinputconfig:
            if model["isSelected"]:
                if model["type"]=='Classification':
                    metrics=pd.DataFrame(columns = ['modelname','accuracy_score','recall_score','precision_score','f1_score','cohen_kappa_score','matthews_corrcoef'])
                
                elif model["type"]=='Regression':
                    metrics=pd.DataFrame(columns=['modelname','mean_absolute_error','mean_squared_error','r2_score','mean_squared_log_error'])
                

                hypers=[]
                keylist=[]
                for feature in model["hyper"]:
                    if feature["ischanged"]:
                        keylist.append(feature["name"])
                        hypers.append(feature["name"]+"="+ str(feature["value"]))
                model_str=model["modelname"] + "(" + ", ".join(hypers) + ")"
    
                metrics=hp.optimize(model_str,model["modelname"],userinputconfig,xdata,ydata,metrics)
