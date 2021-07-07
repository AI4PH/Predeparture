#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


header_list = ["Number of times pregnant", "2 hour plasma glucose concentration", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)","2 hour serum insulin (mu U/ml)", "BMI", "Diabetes pedigree function", "Age (years)", "Diabetes"]
#https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
#the headers list is defined first so that when we import the actual file, we are able to use these to generate the graph

db = pd.read_csv("/Users/josey/Desktop/ChinnuStuff/pima-diabetes.csv", names=header_list)
#https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
#db so that we can use it later, it will work without it but then we would have to redefine

print(db) #generate the table using the db variable. otherwise run the previous line without the 'db=' and it will print graph without this command, but then db is not a variable


# In[3]:


training_data = db.sample(frac=0.8, random_state=42) #42 is seed - it helps to make the random assignment of the data collected into 80% for training and 20% for testing. if another person uses the same seed, they'd get the same 'random' assignment, with another seed, it would be another different random assingment
test_data = db.drop(training_data.index)  #actual test step
# print(test_data) could be used if we wanted to visuablize this


# In[4]:


training_label = training_data.pop("Diabetes")
test_label = test_data.pop("Diabetes")
training_data = training_data[["Number of times pregnant", "2 hour plasma glucose concentration", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)","2 hour serum insulin (mu U/ml)", "BMI", "Diabetes pedigree function", "Age (years)"]]
test_data = test_data[["Number of times pregnant", "2 hour plasma glucose concentration", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)","2 hour serum insulin (mu U/ml)", "BMI", "Diabetes pedigree function", "Age (years)"]]


# In[5]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10) 
random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
decision_tree_model.fit(training_data, training_label)
random_forest_model.fit(training_data, training_label)
 


# In[6]:


from sklearn.metrics import accuracy_score
y_pred_1 = decision_tree_model.predict(test_data)
accuracy_1 = accuracy_score(test_label,y_pred_1)
y_pred_2 = random_forest_model.predict(test_data)
accuracy_2 = accuracy_score(test_label,y_pred_2)
 
#visualize the results
print(accuracy_1)
print(accuracy_2)


# In[7]:


#pull out any one of the many decision trees – it doesn’t need to be the 6th.
estimator = random_forest_model.estimators_[5]
 
from sklearn.tree import export_graphviz
 
# Export as dot file
export_graphviz(estimator, out_file='tree.dot',
            	feature_names = ["Number of times pregnant", "2 hour plasma glucose concentration", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)","2 hour serum insulin (mu U/ml)", "BMI", "Diabetes pedigree function", "Age (years)"],
            	class_names = ["True", "False"],
            	rounded = True, proportion = False,
            	precision = 2, filled = True)
 


# In[8]:


from IPython.display import Image

from subprocess import check_call
 
check_call(['dot', '-Tpng', 'tree.dot', '-o', 'tree2.png', '-Gdpi=600'])
 
Image(filename = 'tree2.png')

