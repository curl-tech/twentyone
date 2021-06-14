from fastapi import FastAPI, Depends, Response, status,HTTPException
from . import schemas, models

app=FastAPI()

@app.get('/')
def home():  
    pass

@app.post('/create',status_code=status.HTTP_202_ACCEPTED)
def create():
    model_type='Classification'
    project_name='A'
    traindata=''
    if(testdata):
        testdata=''
    else:
        testdata=NULL
    #send inputs to db
    #send response to frontend
    
@app.post('/preprocess',status_code=status.HTTP_202_ACCEPTED)
def preprocess():
    pre_pro_auto=True
    target_variable=''
    raw_data_address=''
    model_type='Classification'
    if(pre_pro_auto==False):
        parameters={'':''}
        #send paramters to db
        clean_data_add=manual_preprocess(model_type,raw_data_address,target_variable,parameters)
        #send clean_data pointers to db
    else:
        clean_data_add,parameters=auto_preprocess(model_type,raw_data_address,target_variable)
        #send paramters to db
        #send clean_data pointer to db
    
    #render model selection page 

@app.post('/training',status_code=status.HTTP_202_ACCEPTED)
def models():
    model_auto=True
    model_number=3 #no. of models user wants
    if(model_auto==True):
        Model_list=top_models_auto(model_number)
        #hyperparameter Tuning
        tuned_model_list,hyperparamters=tune_model(Model_list) #auto if model is auto
        #send hyperparamters to db
        # send tuned models pointers to db
    else:
        Model_list_manual=['']       
        Model_list=top_models_manual(model_list_manual)
        #send hyperparamters to db
        if(hyper_auto==True):
            tuned_model_list=tune_model_auto(Model_list)
            # send tuned models pointers to db
        else:
            hyperparamters={'':''}
            #hyperparamter tuning with auto manual option 
            tuned_model_list=tune_model_custom(Model_list,hyperparamaters)#hyperparamter=dictionary  
            # send tuned models pointers to db
            #Metrics calculation
    metrics_list=calculate_metrics(tuned_model_list) 
    # send metrics to db
    
    #send response to frontend  
    

@app.post('/inference',status_code=status.HTTP_202_ACCEPTED)
def inference():
    pass

if __name__=='__main__':
    app.run()