from numpy.core.numeric import NaN
from sklearn.metrics import accuracy_score , recall_score, precision_score, f1_score, cohen_kappa_score, matthews_corrcoef
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,mean_squared_log_error


class Metrics:

    def calculate_metrics(modelname,model_type,prediction,y): # nested list


        if model_type=="Classification":
            criterias=["accuracy_score" , "recall_score", "precision_score", "f1_score", "cohen_kappa_score", "matthews_corrcoef"]
        #metrics.loc[len(metrics.index)]=[modelname,accuracy_score(y,prediction),recall_score(y,prediction),precision_score(y,prediction),f1_score(y,prediction),cohen_kappa_score(y,prediction),matthews_corrcoef(y,prediction)]

        elif model_type=="Regression":
            criterias=["mean_absolute_error","mean_squared_error","r2_score","mean_squared_log_error"]

        metricsnewrow=[modelname]
        for criteria in criterias:
            try:
                metricsnewrow.append(eval(criteria+"(y,prediction)"))

            except:
                metricsnewrow.append("Not Available")
            
        

        return metricsnewrow