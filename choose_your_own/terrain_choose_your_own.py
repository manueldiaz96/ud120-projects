import numpy as np

from sklearn import datasets
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier

import prep_terrain_data

X_train, y_train, X_test, y_test = prep_terrain_data.makeTerrainData()

clf_knn = KNeighborsClassifier(n_neighbors=15  , weights="distance")
clf_knn.fit(X_train, y_train)
predict = clf_knn.predict(X_test)
acc = accuracy_score(y_test, predict)
print("KNeighborsClassifier:", acc)

clf_ada = AdaBoostClassifier(n_estimators=200)
clf_ada.fit(X_train, y_train)
predict = clf_ada.predict(X_test)
acc = accuracy_score(y_test, predict)
print("AdaBoostClassifier:", acc)

clf_rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
clf_rf.fit(X_train, y_train)
predict = clf_rf.predict(X_test)
acc = accuracy_score(y_test, predict)
print("AdaBoostClassifier:", acc)