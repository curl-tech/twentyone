from pycaret.regression import *
# from pycaret.clustering import *
# from pycaret.nlp import *
import os
import pandas as pd
import joblib
import shutil
import yaml
from yaml.loader import SafeLoader
class AutoReg:
    #df = raw_data_address
    #target_col_name = target_col_name
    #problem_type = problem_type
    #na_value = na_value
    #encoding_type=encoding_type
    #encode_col_name=encode_col_name
    #scaling_type = scaling_type
    #scaling_col_name=scaling_col_name
    
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
        
        nlp1 = setup(data = df, target = config["target_col_name"],silent=True)
        X_train = get_config('X_train')    
        X_train.to_csv('clean_data.csv', index=False)
        clean_data_address = os.path.join(os.getcwd(),"clean_data.csv")

        return clean_data_address     


    def top_models_auto(self,config,n=3):

        """
        This funtion takes the user input n in integer format and feeds it to the pycaret function and pycaret in turn returns the top n funtion in an array format 
        The array containing classifiers is returned at the end of the function 
        """
        config=yaml.load(open(config),Loader=SafeLoader)
        best = compare_models()
        request = pull()
        request = request.rename({'Prec.': 'Precision'}, axis='columns')
        request.reset_index(drop=True, inplace=True)
        request.to_csv(os.path.join(config["location"],"metrics.csv"), index=True, index_label="Sno")
        # metrics_address = os.getcwd()+"/metrics.csv"
        # with open (os.path.join(config["location"],"metrics.csv"),'w+') as f:
        #     f.write(request.to_csv('metrics.csv', index=True, index_label="Sno"))
        #     f.close()
        
        return best
    
    


    
    def model_tune(self,model):
        
        # count=0

        tunedmodel=tune_model(model)
            # if(count==2):
            #     break

        return tunedmodel 
    


    def model_save(self,model,config):
        """
        Saves the pkl file at the specified location 
        Ex:
        myfirstexp01_model01.pkl

        here myfirstexp is the name of the experiment started by the user.
        01 is the id or the run number of the test this is inplace made to avoid repetition of names in subsequent runs on the same data set within the experiment
        """
        config=yaml.load(open(config),Loader=SafeLoader)
    
        #/home/rishabh/githubrepos/Project_21-1/Database/Tired_7378399911531481/98686_model0
        location=os.path.join(config["location"],str(config["id"])+"_model")
        os.makedirs(location) ## creates a folder by the name configid_model(number) at the specified location
        # os.makedirs(os.path.join(location,"plots")) ## creates a subfolder named plots to store all the plots inside it
        #Tired98686_model0
        name=str(config["experimentname"])+str(config["id"])+"_model"
        os.makedirs(os.path.join(config["location"],name))
        save_model(model,name)
        shutil.move(name+'.pkl',location) ##moves  the pkl to the respective folders at the specified location 
        shutil.move('clean_data.csv',os.path.join(config["location"],"data"))
        # for i in range(1):
        #     name=str(config["experimentname"])+str(config["id"])+"_model"+str(i)+'.pkl'
        #     save_model(model_array[i],name)
        #     shutil.move(name+".pkl",str(config["location"])+str(config["id"])+"_model"+str(i)) ##moves  the pkl to the respective folders at the specified location 
        #     ## folder name is of the form ex:"01_model1" 

    
    def model_plot(self,model_array,config):
        config=yaml.load(open(config),Loader=SafeLoader)
        if config["problem_type"]=="classification":
            feature_list=["feature","auc","pr","confusion_matrix","error","learning"]
            for i in range(len(model_array)):
                location=os.path.join(config["location"],str(config["id"]),"_model",str(i))
                os.makedirs(location) ## creates a folder by the name configid_model(number) at the specified location
                os.makedirs(os.path.join(location,"plots")) ## creates a subfolder named plots to store all the plots inside it
                plot_list=list(plot_model(model_array[i],feature,save=True) for feature in feature_list)
                for f in plot_list:
                    shutil.move(f, os.path.join(location,"plots"))

        if config["problem_type"]=="regression":
            feature_list=["feature","residuals","cooks","vc","error","learning"]
            for i in range(len(model_array)):
                location=os.path.join(config["location"],str(config["id"])+"_model"+str(i))
                os.makedirs(location)
                os.makedirs(os.path.join(location,"plots"))
                plot_list=list(plot_model(model_array[i],feature,save=True) for feature in feature_list)
                for f in plot_list:
                    shutil.move(f, os.path.join(location,"plots"))
        

    

    def auto(self,config):
        config2=yaml.load(open(config),Loader=SafeLoader)
        clean_data=self.auto_setup(config)
        model=self.top_models_auto(config,config2["n"])
        tunedmodel=self.model_tune(model)

        print("Model List:",model)
        print("Tuned List: ",tunedmodel)
        # self.model_plot(tunedmodel,config)
        self.model_save(tunedmodel,config)
        