import joblib
from pycaret.classification import *
from pycaret.regression import *
import pandas as pd
import os

class inference:
    def inference(isAuto,filelocation,data_location,storelocation):
        
    
        data=pd.read_csv(data_location)
        clf=load_model(filelocation)
        results=predict_model(clf,data=data)

        csvresults=results.to_csv()

        inference=open(os.path.join(storelocation,"inference.csv"),"w+")
        inference.write(csvresults)
        inference.close()
    