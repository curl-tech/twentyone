import numpy as np
import pandas as pd
import types
import sys

from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.datasets.base import load_iris

def str_to_class(field):
    try:
        identifier = getattr(sys.modules[__name__], field)
    except AttributeError:
        raise NameError("%s doesn't exist." % field)
    if isinstance(identifier, types.ClassType):
        return identifier
    raise TypeError("%s is not a class." % field)

models = ["SVC", "LogisticRegression", "DecisionTreeClassifier", "KNeighborsClassifier"]

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
        model = str_to_class(model_str)()
        model.fit(train_X, train_y)
        prediction=model.predict(test_X)
        print(f'The accuracy of the {model_str} is', metrics.accuracy_score(prediction, test_y))







