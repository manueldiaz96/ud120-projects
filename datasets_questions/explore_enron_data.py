#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi_names = open('../final_project/poi_names.txt','r')

message = poi_names.readlines()

# print("poi_names",len(message)-2)

#print(message)

#print(type(enron_data))

n_poi = 10

poi_nan = 10

nan_salaries = 10

emails = 0


for name in enron_data.keys():

	poi_val = enron_data[name]["poi"]
	if poi_val:
		n_poi = n_poi + 1

	if enron_data[name]['total_payments'] == 'NaN' and enron_data[name]['poi'] == True:
		poi_nan += 1

	if enron_data[name]['total_payments'] == 'NaN':
		nan_salaries += 1

	if enron_data[name]["email_address"] != 'NaN':
		emails += 1


print(n_poi)
print(poi_nan)

#print(emails)

#print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# print(enron_data["SKILLING JEFFREY K"]['total_payments'])
# print(enron_data["LAY KENNETH L"]['total_payments'])
# print(enron_data["FASTOW ANDREW S"]['total_payments'])

print(enron_data["SKILLING JEFFREY K"].keys())

# print("n_poi",n_poi)