#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for key, value in data_dict.items():
    if value['bonus'] == data.max():
        print (key, data.max())
        outlier = key

data_dict.pop(outlier, 0)

data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )



matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")



biggest = [0,0]
for key, value in data_dict.items():
    if value['bonus'] > 0.4e7 and value['salary'] > 1e6 and value['bonus'] !='NaN':
    	print key 


matplotlib.pyplot.show()