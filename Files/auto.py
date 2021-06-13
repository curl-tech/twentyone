from pycaret.classification import *
from pycaret.regression import *
# from pycaret.clustering import *
# from pycaret.nlp import *
import os
import pandas as pd

class auto:
    df = raw_data_address
    target_col_name = target_col_name
    problem_type = problem_type
    na_value = na_value
    encoding_type=encoding_type
    encode_col_name=encode_col_name
    scaling_type = scaling_type
    scaling_col_name=scaling_col_name
    
    def auto_setup(problem_type,raw_data_address,target_col_name):   
        """
        This function is for preprocessing the data when the user selects auto.
    
        Extended description of function:-
        Parameters:
            problem_type (string):          (The selection of the user for the model_type eg-classification/regression/clustering etc.)
            raw_data_address (string):    (As the user uploads the raw dataset it will be saved in the database, this is the address of that saved dataset.)
            target_col_name (string):     (The user will select the target cloumn/variable and that target variable name have to be passed to the setup() in pycaret as patameter.)
            
        """
        if problem_type == "classification":
            clf1 = setup(data = raw_data_address, target = target_col_name,silent=True, profile= True)
        elif problem_type== "regression":
            reg1 = setup(data = raw_data_address, target = target_col_name,silent=True, profile= True)
        elif problem_type == "clustering":
            clu1 = setup(data = raw_data_address,silent=True, profile= True)
        elif problem_type == "nlp":
            nlp1 = setup(data = raw_data_address, target = target_col_name,silent=True, profile= True)
        X_train = get_config('X_train')

        X_train.to_csv('clean_data.csv', index=False)
        clean_data_address = os.getcwd()+"/clean_data.csv"

        return clean_data_address     
    
    def top_models_auto(self,n=3):

        """
        This funtion takes the user input n in integer format and feeds it to the pycaret function and pycaret in turn returns the top n funtion in an array format 
        The array containing classifiers is returned at the end of the function 
        """
        best = compare_models(n)
        return best


    
    def model_tune(self,model_array):
        tuned_best=[]
        for i in model_array:
            tuned_best.append(tune_model(i))

        return tuned_best

