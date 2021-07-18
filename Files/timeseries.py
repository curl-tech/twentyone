from pmdarima import auto_arima
#from fbprophet import Prophet
import json
#from fbprophet.serialize import model_to_json, model_from_json
import os
import yaml
from yaml.loader import FullLoader
import plotly
import pandas as pd
import plotly.express as ex

from Files.metrics import Metrics as met
class timeseries:
    def createprophet(dataconfig):
        with open(dataconfig) as f:
            dataconfigfile= yaml.load(f,Loader=FullLoader)
        data=dataconfig["data"]
        location=dataconfig["location"]
        model=Prophet()
        testsize=int(len(data)*0.2)
        train=data.iloc[:-testsize]
        test=data.iloc[-testsize:]
        model.fit(train)
        pred=model.predict(test)
        pred=pred.yhat
        actual=test.y

        metrics=met.calculate_metrics("fbprophet","Regression",pred,actual)
        metricsLocation=os.path.join(dataconfigfile["location"],"metrics.csv")
        metrics.to_csv(metricsLocation, index=True)

        compare=pd.DataFrame(pred.values,columns=['predictions'])
        compare['actual']=actual.values
        print(compare)
        fig=compare.plot(legend=True)
        plotly.offline.plot(fig,filename=os.path.join(location,"fbtestvspred.html"))

        modelfinal=Prophet()
        modelfinal.fit(data)
        location="serialized_model.json"
        location=os.path.join(dataconfigfile['location'],str(dataconfigfile['projectname'])+str('fb'))
        with open(location, 'w') as fout: #save the model
            json.dump(model_to_json(modelfinal), fout)
        return location

    def fbinference(location,number):
        with open(location, 'r') as fin:
            model = model_from_json(json.load(fin))
        future=model.make_future_dataframe(periods=number)
        pred=model.predict(future)
        return pred

    def createarima(dataconfig):
        with open(dataconfig) as f:
            dataconfigfile= yaml.load(f,Loader=FullLoader)

        data=dataconfig["data"]
        location=dataconfig["location"]
        testsize=int(len(data)*0.2)
        train=data.iloc[:-testsize]
        test=data.iloc[-testsize:]
        model = auto_arima(train['y'],trace=True) 
        testpred=model.predict(testsize)
        testactual=test.y

        metrics=met.calculate_metrics("fbprophet","Regression",testpred,testactual)
        metricsLocation=os.path.join(dataconfigfile["location"],"metrics.csv")
        metrics.to_csv(metricsLocation, index=True)
        compare=pd.DataFrame(testpred,columns=['predictions'])
        compare['actual']=testactual.values

        fig=compare.plot(legend=True)
        plotly.offline.plot(fig,filename=os.path.join(location,"arimatestvspred.html"))
        modelfinal=auto_arima(data['y'], trace=True,suppress_warnings=True)
        return metricsLocation