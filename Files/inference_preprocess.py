import numpy as np
import pandas as pd

# Handling missing data using-
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

# Scaling and Teansforming using- 
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
 
# Handling non-numeric data using-
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder 

from pycaret.classification import *
from pycaret.regression import *
# from pycaret.clustering import *
# from pycaret.nlp import *
import os
import yaml
from scipy import stats

class Preprocess:     
    def inference_preprocess(self,config):
        """
        This function is for preprocessing the data when the user selects manual preprocessing.                     
        """
        config = open("preprocess_config.yaml", 'r')
        config_data = yaml.safe_load(config)

        
        df = pd.read_csv(config_data["inference_data"])
               
        def drop_NA(df):
            # On calling this function it drops all the columns and rows which are compleatly null.
            nan_value = config_data["na_notation"]
            df.replace("", nan_value, inplace=True)
            df = df.dropna(how='all', axis=1, inplace=True)
            df = df.dropna(how='all', inplace=True)
            
        if config_data['drop_column_name'][0] != None:
            df=df.drop(config_data["drop_col_name"], axis = 1)
            drop_NA(df)
        else:
            drop_NA(df)

        # imputation
        if config_data['imputation_column_name'][0] != None:
            for index, column in enumerate(config_data["imputation_column_name"]):
                replace_value = config_data["mean_median_mode_values"][index] 
                
                df[column].replace(to_replace =[config_data["na_notation"]],value = replace_value)
                
                type = config_data["impution_type"][index] 
                if type=='knn':
                    df_value = df[[column]].values
                    imputer = KNNImputer(n_neighbors = 4, weights = "uniform",missing_values = config_data["na_notation"])
                    df[[column]] = imputer.fit_transform(df_value)
        
        elif config_data['imputation_column_name'][0] == None:
            for col_name in df.columns:
                if df[col_name].dtype == 'object':
                    df.replace(to_replace =[config_data["na_notation"]],value ="No data")
                else:
                    df.replace(to_replace =[config_data["na_notation"]],value =0)
            
        #feature scaling
        if config_data['scaling_column_name'][0] != None:
            for index, column in enumerate(config_data["scaling_column_name"]):
                type = config_data["scaling_type"][index]                
                df_value = df[[column]].values

                if type == "normalization":
                    
                    df_std = (df_value - df_value.min(axis=0)) / (df_value.max(axis=0) - df_value.min(axis=0))
                    scaled_value = df_std * (1 - 0)
                    config_data['scaling_type'][index] = {config_data['scaling_type'][index]:{"min":df_value.min(axis=0),"max":df_value.max(axis=0)}}
                    
                    
                elif type == 'standarization':
                    df_std = (df_value - df_value.min(axis=0)) / (df_value.max(axis=0) - df_value.min(axis=0))
                    scaled_value = (df_value - df.value.mean()) / df_std 
                    config_data['scaling_type'][index] = {config_data['scaling_type'][index]:{"std":df_std,"mean":df.value.mean()}}
                    
                df[[column]] = scaled_value
                
   
        #### handling catogarical data
        # encoding
        # Under the following if block only the columns selected by the used will be encoded as choosed by the used. 
        if config_data['encode_column_name'][0] != None:
            for index, column in enumerate(config_data["encode_column_name"]):
                type = config_data["encoding_type"][index]
                
                                    
                if type == "Label Encodeing":
                    encoder = LabelEncoder()
                    df[column] = encoder.fit_transform(df[column])

                elif type == "One-Hot Encoding":
                    encoder = OneHotEncoder(drop = 'first', sparse=False)
                    df_encoded = pd.DataFrame (encoder.fit_transform(df[[column]]))
                    df_encoded.columns = encoder.get_feature_names([column])
                    df.drop([column] ,axis=1, inplace=True)
                    df= pd.concat([df, df_encoded ], axis=1)
                    
        # Feature engineering & Feature Selection
        ### Outlier detection & Removel
        # We are removing the outliers if on the basis on z-score.

        if config_data["Remove_outlier"] == True:
            z = np.abs(stats.zscore(df))
            df = df[(z < 3).all(axis=1)]
              
        # Here we are selecting the column which are having more then 70 correlation.
        if config_data["feature_selection"] == True:
            col_corr = set()
            corr_matrix = df.corr()
            for i in range(len(corr_matrix.columns)):
                    for j in range(i):
                        if abs(corr_matrix.iloc[i, j]) > 0.70:
                            col_corr.add(corr_matrix.columns[i])
                                        
            df = df.drop(col_corr,axis=1)

            # with the following function we can select highly correlated features
            # it will remove the first feature that is correlated with anything other feature

        # Droping the columns which are left behind and can cause problem at the time of model training.
        for col_name in df.columns:
            if df[col_name].dtype == 'object':
                df=df.drop(col_name, axis = 1)

        with open("preprocess_config.yaml", 'w') as yaml_file:
            yaml_file.write( yaml.dump(config_data, default_flow_style=False))

        clean_data_address = os.getcwd()+"/clean_data.csv"
        return clean_data_address
    