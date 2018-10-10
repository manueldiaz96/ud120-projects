#!/usr/bin/python

import numpy as np

from sklearn import datasets
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=np.random.randint(1))

# http://scikit-learn.org/stable/modules/ensemble.html

print("AdaBoostClassifier")

clf_ada = AdaBoostClassifier(n_estimators=100) #Number of how many weak classificators

print("Done")

clf_ada.fit(X_train, y_train)

predict = clf_ada.predict(X_test)

acc = accuracy_score(y_test, predict)

print(acc)