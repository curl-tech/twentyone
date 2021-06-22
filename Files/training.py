from pycaret.classification import *
from pycaret.regression import *
import json
import yaml
from yaml.loader import SafeLoader

class training:
    def training(self,model_array,Xdata,Ydata):
        with open("model.yaml") as f:
            model_uni= yaml.load(f,Loader=SafeLoader)
        
        data=json.loads(model_array)
        for i in data:
            if i["ishyper"]:
                
