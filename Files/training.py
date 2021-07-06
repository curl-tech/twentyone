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
import os


class training:

    def train(userinputconfig,dataconfig,preprocessconfig):

        with open(preprocessconfig) as f:
            preprocessconfigfile= yaml.load(f,Loader=FullLoader) #for split ratio
        

        with open(dataconfig) as f:
            dataconfigfile= yaml.load(f,Loader=FullLoader) #has info about where the data is stored and where the model must be stored

        with open(userinputconfig) as file:
            userinputconfigfile=yaml.load(file,Loader=FullLoader) #modified version of model universe for each run
        models=[]
        ans=[]

        test_ratio=preprocessconfigfile["split_ratio_test"] #input given the the user usually 30 by default
        
        xdata=dataconfigfile["Xdata"] #the location of the x data

        ydata=dataconfigfile["Ydata"] #the location of the y data
        
        #creates a pandas dataframe to store the metrics of the created model
        for model in userinputconfigfile:
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
    
                metrics=hp.optimize(model_str,model["modelname"],userinputconfig,xdata,ydata,metrics,dataconfig)

        #stores the metrics in the assigned folder       
        metricsLocation=os.path.join(dataconfig["location"],"metrics.csv")
        metrics.to_csv(metricsLocation, index=True, index_label="modelname")
