from pycaret.classification import *
from pycaret.regression import *
# from pycaret.clustering import *
# from pycaret.nlp import *
import os
class auto:
    def preprocess(model_type,raw_data_address,target_variable):
        """
        This function is for preprocessing the data when the user selects auto preprocessing.
    
        Extended description of function:-
        Parameters:
            model_type (string):          (The selection of the user for the model_type eg-classification/regression/clustering etc.)
            raw_data_address (string):    (As the user uploads the raw dataset it will be saved in the database, this is the address of that saved dataset.)
            target_variable (string):     (The user will select the target cloumn/variable and that target variable name have to be passed to the setup() in pycaret as patameter.)
            
        Returns:
            clean_data_address(string): 
        """
        
        if model_type == "classification":
            clf1 = setup(data = raw_data_address, target = target_variable,silent=True, profile= True)
        
        elif model_type == "regression":
            reg1 = setup(data = raw_data_address, target = target_variable,silent=True, profile= True)

        # elif model_type == "clustering":            
        #     clu1 = setup(data = raw_data_address,silent=True, profile= True)

        # elif model_type == "nlp":            
        #     nlp1 = setup(data = raw_data_address, target = target_variable,silent=True, profile= True)
        
        X_train = get_config('X_train')        
        
        X_train.to_csv('clean_data.csv', index=False)
        
        clean_data_address = os.getcwd()+"/clean_data.csv"
        return clean_data_address
        
    def
     