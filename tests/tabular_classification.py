import numpy as np
import pandas as pd
import types
import sys

from sklearn.model_selection import train_test_split
from sklearn import metrics

sys.path.append("src")

from models.load_lib import *

from sklearn.datasets.base import load_iris

models = ["SVC", "LogisticRegression", "DecisionTreeClassifier", "KNeighborsClassifier"]
params = ["kernel='linear', C=0.025"]

if __name__ == "__main__":
    iris = load_iris()
    obs = iris.data
    target = iris.target

    iris_df = pd.DataFrame(obs, columns=iris.feature_names)
    iris_df["target_"] = target

    train, test = train_test_split(iris_df, test_size = 0.3)

    train_X  = train[iris.feature_names]
    train_y  = train["target_"]
    test_X  = test[iris.feature_names]
    test_y  = test["target_"]

    for model_str in models:
        model = eval(model_str+"()")
        model.fit(train_X, train_y)
        prediction=model.predict(test_X)
        print(f'The accuracy of the {model_str} is', metrics.accuracy_score(prediction, test_y))
