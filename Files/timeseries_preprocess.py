import shutil
import pandas as pd
from pandas.core.frame import DataFrame

from sklearn.preprocessing import OneHotEncoder 
from yaml.loader import SafeLoader
import os
import yaml
from scipy import stats

class TimeseriesPreprocess:     
    def preprocess(self,config,folderLocation):

        
        config_data=yaml.load(open(config),Loader=SafeLoader)
        
        df = pd.read_csv(config_data["raw_data_address"])
        
        df.dropna(how='all', axis=1, inplace=True)
        
        print("DataFrame again: ", df)
        df.set_index(config_data['date_index'], inplace = True)
        df.index=pd.to_datetime(df.index,format = config_data['date_format']) 
        # df = df['Cases'].resample(config_data['frequency']).sum()


        # df.index=pd.to_datetime(df.index,format ='%Y-%m-%d') 
        
        # if config_data['frequency'] is not None:
        #     df = df.asfreq(freq = config_data["frequency"], method='bfill',normalize=True)
        
        df = df.fillna(method='bfill')
    
        df.rename(columns = {config_data['date_index']:'ds', config_data['target_column_name']:'y'}, inplace = True)

        df['Date'] = df.index

        object_type_column_name = []
        for col_name in df.columns:
            if df[col_name].dtype == 'object':
                object_type_column_name.append(col_name)
                config_data['encoding_type'].extend(['One-Hot Encoding'])

        print("object type column name: ",object_type_column_name)
        if object_type_column_name != [] :
            config_data['encode_column_name'] = object_type_column_name

            encoder = OneHotEncoder(drop = 'first', sparse=False)
            df_encoded = pd.DataFrame (encoder.fit_transform(df[object_type_column_name]))
            df_encoded.columns = encoder.get_feature_names([object_type_column_name])
            df.drop([object_type_column_name] ,axis=1, inplace=True)
            df= pd.concat([df, df_encoded ], axis=1)                 
            
        df.to_csv('clean_data.csv')
        shutil.move("clean_data.csv",folderLocation)
        clean_data_address = os.path.abspath(os.path.join(folderLocation,"clean_data.csv"))
        config_data['clean_data_address'] = clean_data_address
    
    
    
        with open(config, 'w') as yaml_file:
            yaml_file.write( yaml.dump(config_data, default_flow_style=False))

        return clean_data_address