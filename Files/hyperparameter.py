from pycaret.classification import *
from pycaret.regression import *

class hyperparameter:
    def __init__(self):
        self.parameters={} ## only valid for custom models
    
    def tune_model_auto(self,modellist):
        tuned_model_list=[tune_model(i) for i in modellist]  ## model list is the list of classifiers passed in an array format
        self.model_list=tuned_model_list
        return tuned_model_list

    def tune_model_custom(self,modellist,parameters):
        tuned_list=[]
        for i in range(len(modellist)):
            tuned_model=tune_model(modellist[i],custom_grid=parameters[i])
            tuned_list.append(tuned_model)
        return tuned_list

    



