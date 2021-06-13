from pycaret.classification import *
from pycaret.regression import *
from ray import tune 

class training:
    def __init__(self):
        self.name=""
    def top_models_auto(self,n): # n is the number of top models we need to return according to the user
        top_nmodels=compare_models(n_select=n)
        return top_nmodels

    def top_models_custom(self,models_name_list): #names of the model in pycaret conventions
        modellist=[]
        for model_name in models_name_list:
            new_model=create_model(model_name)
            modellist.append(new_model)

        return modellist