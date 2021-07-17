import numpy as np
import pandas as pd

from datetime import datetime
from sklearn.preprocessing import OneHotEncoder 

import os
import yaml
from scipy import stats

class Preprocess:     
    def preprocess(self,config):

        config = open("preprocess_config.yaml", 'r')
        config_data = yaml.safe_load(config)
        
        df = pd.read_csv(config_data["raw_data_address"])
        
        # The following line will be used if the user want's to remove all the exoginous columns. 
        # df = df[[config_data['data_index_column'],config_data['target_column_name']]]
        # df[config_data['data_index_column']] = pd.to_datetime(df[config_data['data_index_column']]).dt.strftime(config_data['date_format'])
        
        df = df.dropna(how='all', axis=1, inplace=True)
        
        if config_data['frequency'] != None:
            df = df.asfreq(freq = config_data["frequency"], method='bfill',normalize=True)
        
        df = df.fillna(method='bfill')
    
        objest_type_column_list = []
        for col_name in df.columns:
            if df[col_name].dtype == 'object':
                objest_type_column_list.append(col_name)
                config_data['encodeing_type'].extend(['One-Hot Encoding'])
                
        if objest_type_column_list != [] :
            config_data['encode_column_name'] = objest_type_column_list

            encoder = OneHotEncoder(drop = 'first', sparse=False)
            df_encoded = pd.DataFrame (encoder.fit_transform(df[objest_type_column_list]))
            df_encoded.columns = encoder.get_feature_names([objest_type_column_list])
            df.drop([objest_type_column_list] ,axis=1, inplace=True)
            df= pd.concat([df, df_encoded ], axis=1)                 
            
            
            
            
            
        df.set_index('Month', inplace=True)            
        
        clean_data_address = os.getcwd()+"/clean_data.csv"
        config_data['clean_data_address'] = clean_data_address
    
        with open("preprocess_config.yaml", 'w') as yaml_file:
            yaml_file.write( yaml.dump(config_data, default_flow_style=False))
