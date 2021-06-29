import yaml
from yaml.loader import FullLoader
import numpy as np
import pandas as pd
import json
import pickle
import pandas as pd
from .libraries import *
from Files.metrics import Metrics as met
class hyperparameter:
    def optimize(model_str,modelname,userinputconfig,xdata,ydata,metrics,dataconfig):
        """
        This function in takes the string consisting of the name and the hyperparameters of the model and uses eval function to create the model.
        Keylist is the dictionary consisting of the infomation about the user input ('subject to further changes')
        Name is the name of the model selected (subject to future changes)
        """

        xdata=pd.read_csv(xdata)
        ydata=pd.read_csv(ydata)
        with open(userinputconfig) as f:
            userinputconfig= yaml.load(f,Loader=FullLoader)

        with open(dataconfig) as c:
            dataconfig=yaml.load(c,Loader=FullLoader)

        params={}
        for model in userinputconfig:
            if model["isSelected"]:
                modeltype=model["type"]
                for hyper in model["hyper"]:
                    if hyper["ischanged"]==False:
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
        x_train,x_test,y_train,y_test=train_test_split(xdata,ydata,test_size=0.2)
        clf.fit(x_train,y_train)

        
        pickle.dump(clf)
        prediction=clf.predict(x_test)
        metrics=met.calculate_metrics(modelname,modeltype,metrics,prediction,y_test)
        return metrics