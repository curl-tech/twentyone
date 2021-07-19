from preprocess import *
from training import *
from hyperparameter import *
from metrics import *
class main:
    pre_pro_auto=True
    model_auto=True
    hyper_auto=True
    model_type='Classification'
    models_number=5
    model_list_manual=[]
    # def __init__(self,apre_pro_auto,amodel_auto,ahyper_auto,amodel_type,amodel_number):
    #     self.pre_pro_auto=apre_pro_auto
    #     self.model_auto=amodel_auto
    #     self.hyper_auto=ahyper_auto
    #     self.model_type=amodel_type
    #     self.models_number=amodel_number

    def main2():
        """ Main program """
        #Preprocessing
        if(pre_pro_auto==True):
            clean_data_add=auto_preprocess(model_type,raw_data_address,target_variable)
        else:
            clean_data_add=manual_preprocess(model_type,raw_data_address,target_variable,parameters)
        #Training
        if(model_auto==True):
            Model_list=top_models_auto(model_number)
            #hyperparameter Tuning
            tuned_model_list=tune_model(Model_list) #auto if model is auto
        else:
            Model_list=top_models_manual(model_list_manual)
            #hyperparamter tuning with auto manual option
            if(hyper_auto==True):
                tuned_model_list=tune_model_auto(Model_list)
            else:
                tuned_model_list=tune_model_custom(Model_list,hyperparamaters)#hyperparamter=dictionary    
        #Metrics calculation
        metrics_list=calculate_metrics(tuned_model_list) 
        
        return 0

    if __name__ == "__main__":
        main()