#!/usr/bin/env python
# coding: utf-8

# In[55]:


#Disclaimer: in all honesty, I really struggled with this assignment LOl and I feel like my code is sketchy hahah, I tried my best to explain the steps but it took forever to even get things functioning...


# In[56]:


import geopandas as gpd
import pandas as pd
import csv


# In[57]:


#step 1: Importing and reading data

datadiabetes = pd.read_csv("C:/Users/ST/Downloads/pima-diabetes.csv", header=0)


# In[58]:


#step 2: making headers- this was semi sketchy to figure out, but tried it anyways

datadiabetes.columns = ["Pregnancy number", "2 hr plasma glucose conc", "Diastolic BP", "Triceps skin fold thickness","2 hour serum insulin", "BMI", "Diabetes pedigree function", "Age", "Diabetes"]


# In[59]:


#step 3: as we did in tutorial, divide data into 80% training data and 20% testing data

training_data = datadiabetes.sample(frac=0.8, random_state=42)

test_data = datadiabetes.drop(training_data.index)

print(training_data)


# In[60]:


#step 4: again, following the tutorial, prepare the training and test data

training_label = training_data.pop("Diabetes")

test_label = test_data.pop("Diabetes")


# In[61]:


#step 5:create and train decision tree and random forest models!!!!

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)

random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)

decision_tree_model.fit(training_data, training_label)

random_forest_model.fit(training_data, training_label)


# In[62]:


#step 6: make predictions
from sklearn.metrics import accuracy_score

y_pred_1 = decision_tree_model.predict(test_data)

accuracy_1 = accuracy_score(test_label,y_pred_1)

y_pred_2 = random_forest_model.predict(test_data)

accuracy_2 = accuracy_score(test_label,y_pred_2)


# In[63]:


#step 7: visualize the accuracy results

print(accuracy_1)

print(accuracy_2)


# In[64]:


#step 8: make the tree!! - this took me so long, but was SO SATISFYING when it finally worked! yay!

estimator = random_forest_model.estimators_[5]

from sklearn.tree import export_graphviz
from subprocess import check_call
from IPython.display import Image

export_graphviz(estimator, out_file="subsA2_tree.dot", 
                feature_names = ["Pregnancy number", "2 hr plasma glucose conc", "Diastolic BP", "Triceps skin fold thickness","2 hour serum insulin", "BMI", "Diabetes pedigree function", "Age"],
                class_names = ["True", "False"],
                rounded = True, proportion = False,
                precision = 2, filled = True)

Image(filename = 'subsA2_tree.png')

