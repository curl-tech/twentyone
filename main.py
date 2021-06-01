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
    def __init__(self,pre_pro_auto,model_auto,hyper_auto,model_type):
        self.pre_pro_auto=pre_pro_auto
        self.model_auto=model_auto
        self.hyper_auto=hyper_auto
        self.model_type=model_type
        models

    def main():
        """ Main program """
        if(pre_pro_auto==True):
            auto_preprocess()
        else:
            manual_preprocess()
        if(model_auto==True):
            if(model_type=='Classification'):
                Model_list=top_models_Classification(model_number)
            elif(model_type=='Regression'):
                Model_list=top_models_Regression(model_number)
            tune_model(Model_list)
        calculate_metrics()
         
        
        return 0

    if __name__ == "__main__":
        main()