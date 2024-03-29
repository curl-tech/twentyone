import pickle
from pycaret.classification import *
from pycaret.regression import *
import pandas as pd
import os
import random

class Inference:
    def inference(self,pickleFileLocation,newDataLocation,storeLocation,isAuto):    #isAuto parameter removed because of error
        
        if isAuto:
            data=pd.read_csv(newDataLocation)
            clf=load_model(pickleFileLocation)
            results=predict_model(clf,data=data)

            csvresults=results.to_csv()
            ran=random.randint(100,999)
            inferenceDataResultsPath=os.path.join(storeLocation,"inference"+str(ran)+".csv")
            inference=open(inferenceDataResultsPath,"w+")
            inference.write(csvresults)
            inference.close()
        
            return inferenceDataResultsPath
        
        else:
            data=pd.read_csv(newDataLocation)
            clf=pickle.load(open(pickleFileLocation,"r"))
            predictions=clf.predict(data)
            results=pd.DataFrame(data)
            results["predictions"]=predictions

            csvresults=results.to_csv()
            ran=random.randint(100,999)
            inferenceDataResultsPath=os.path.join(storeLocation,"inference"+str(ran)+".csv")
            inference=open(inferenceDataResultsPath,"w+")
            inference.write(csvresults)
            inference.close()
        
            return inferenceDataResultsPath