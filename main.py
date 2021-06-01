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

    def main():
        """ Main program """
        #Preprocessing
        if(pre_pro_auto==True):
            auto_preprocess()
        else:
            manual_preprocess()
        #Training
        if(model_auto==True):
            if(model_type=='Classification'):
                Model_list=top_models_Classification(model_number)
            elif(model_type=='Regression'):
                Model_list=top_models_Regression(model_number)
            #hyperparameter Tuning
            tune_model(Model_list) #auto if model is auto
        else:
            if(model_type=='Classification'):
                Model_list=top_models_Classification_manual(model_number,model_list_manual)
            elif(model_type=='Regression'):
                Model_list=top_models_Regression_manual(model_number,model_list_manual)
            #hyperparamter tuning with auto manual option
            if(hyper_auto==True):
                tune_model(Model_list)
            else:
                tune_custom_model(Model_list)    
        #Metrics calculation
        calculate_metrics() 
        
        return 0

    if __name__ == "__main__":
        main()