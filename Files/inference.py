import joblib
from pycaret.classification import *
from pycaret.regression import *
import pandas as pd
import os

class inference:
    def inference(isAuto,location,data_location,name):
        
        if isAuto:
            data=pd.read_csv(data_location)
            clf=load_model(os.path.join(location,name).replace("\\","/"))
            results=predict_model(clf,data=data)

            csvresults=results.to_csv()

            inference=open(os.path.jois(location,"inference.csv").replace("\\","/"),"w+")
            inference.write(csvresults)
            inference.close()
            return results.to_html()
        else:
            pass