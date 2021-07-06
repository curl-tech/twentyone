from pycaret.clustering import *
import os
import pandas as pd
import joblib
import shutil
import yaml
from yaml.loader import SafeLoader

class Autoclu:
    def auto_setup(self,config):   
        """
        This function is for preprocessing the data when the user selects auto.
    
        Extended description of function:-
        Parameters:
            problem_type (string):          (The selection of the user for the model_type eg-classification/regression/clustering etc.)
            raw_data_address (string):    (As the user uploads the raw dataset it will be saved in the database, this is the address of that saved dataset.)
            target_col_name (string):     (The user will select the target cloumn/variable and that target variable name have to be passed to the setup() in pycaret as patameter.)
            
        """
        config=yaml.load(open(config),Loader=SafeLoader)
        df = pd.read_csv(config["raw_data_address"])
        
        clu = setup(data = df, normalize = True ,silent=True)
        # X_train = get_config()    
        X_train=df
        X_train.to_csv(os.path.join(config["location"],'clean_data.csv'), index=False)
        clean_data_address = os.path.join(config["location"],"clean_data.csv")

        return clean_data_address     

    def model_create(self,config,type="kmeans"):
        config=yaml.load(open(config),Loader=SafeLoader)
        model=create_model(type)
        assignedlabels=assign_model(model)
        resultLocation=os.path.join(config["location"],"assignedlabels.csv")
        assignedlabels.to_csv(resultLocation,index=True)
        return model, resultLocation



    def model_save(self,model,config):
        """
        Saves the pkl file at the specified location 
        Ex:
        myfirstexp01_model01.pkl

        here myfirstexp is the name of the experiment started by the user.
        01 is the id or the run number of the test this is inplace made to avoid repetition of names in subsequent runs on the same data set within the experiment
        """
        config=yaml.load(open(config),Loader=SafeLoader)
    
        location=os.path.join(config["location"],str(config["id"])+"_model")
        os.makedirs(location) ## creates a folder by the name configid_model(number) at the specified location
        # os.makedirs(os.path.join(location,"plots")) ## creates a subfolder named plots to store all the plots inside it
        name=str(config["experimentname"])+str(config["id"])+"_model"
        save_model(model,name)
        shutil.move(name+'.pkl',location) ##moves  the pkl to the respective folders at the specified location 
        # shutil.move('clean_data.csv',os.path.join(config["location"],"data"))
        # for i in range(1):
        #     name=str(config["experimentname"])+str(config["id"])+"_model"+str(i)+'.pkl'
        #     save_model(model_array[i],name)
        #     shutil.move(name+".pkl",str(config["location"])+str(config["id"])+"_model"+str(i)) ##moves  the pkl to the respective folders at the specified location 
        #     ## folder name is of the form ex:"01_model1" 
        return location, os.path.join(location,name)

    
    def model_plot(self,model,location):
        shutil.move(plot_model(model,save=True),location)
        return location

    def auto(self,config):
        try:
            config2=yaml.load(open(config),Loader=SafeLoader)
            cleanDataPath=self.auto_setup(config)
            model, resultLocation=self.model_create(config,config2["clusteringType"])
            # self.model_plot(tunedmodel,config)
            pickleFolderPath, pickleFilePath=self.model_save(model,config)

            plotFolderPath=self.model_plot(model,pickleFolderPath)
            return {"Successful": True, "cleanDataPath": cleanDataPath, "resultPath":resultLocation, "pickleFolderPath":pickleFolderPath, "pickleFilePath":pickleFilePath}

            
        except Exception as e:
            print("An Error Occured: ",e)
            return {"Successful": False, "Error": e}
        