#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
with open("C:/Users/jocel/AppData/Local/Programs/Python/Python39/pima-diabetes.csv", newline='') as csvfile:
   pima_data = csv.reader(csvfile, delimiter=',')

#As a preface to my lines of code in this assignment, I took what you (Dr. Burns), said about challenging yourself to your level of ability in this assignment.
#I wanted to understand/explain to the best of my ability what was happening in each line of code that is in this assignment. 
#There are a few lines I am not sure about (ended those with question marks), but I was using that as an exercise in being able to explain step-by-step what we did. 


# In[2]:


#Step 1: Divide the data into 80% for training and 20% for testing
from numpy.random import RandomState #importing a library called RandomState #Source: https://stackoverflow.com/questions/43697240/how-can-i-split-a-dataset-from-a-csv-file-for-training-and-testing
import pandas #importing library
header_list = ["Number of times pregnant", "Plasma glucose conc", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)", "2-hour serum insulin (mu U/ml)","BMI (kg/m^2)", "Diabetes pedigree function","Age (yrs)","Diabetes"] #creating header names for table of data #Source:https://www.kite.com/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python
df = pandas.read_csv("C:/Users/jocel/AppData/Local/Programs/Python/Python39/pima-diabetes.csv", names=header_list) #pandas structures data,takes csv file and converts to chart 
rng = RandomState(42) #creating a random number generator, 42 is a 'seed', a starting point for the computer. Can put in any number you want

training_data = df.sample(frac=0.8, random_state=rng) #taking a random sample of the dataset (80%) for training data
test_data = df.loc[~df.index.isin(training_data.index)] #taking the remaining 20% and putting it into a model, using it for testing purposes


# In[3]:


print(df) #print DataFrame, shows the data file with added headings 


# In[4]:


#Step 2: Prepare the training and test data
training_label = training_data.pop("Diabetes") #takes Diabetes column out of list of variables in the training data sample, you don't want the outome (Diabetes or not) to train the model 
test_label = test_data.pop("Diabetes") #takes Diabetes column out of the list of variables in the test data sample, you don't want the outome (Diabetes or not) to train the model
training_data = training_data[["Number of times pregnant", "Plasma glucose conc", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)", "2-hour serum insulin (mu U/ml)","BMI (kg/m^2)", "Diabetes pedigree function","Age (yrs)"]] #this shows the list of variables/data columns that are in the training data sample
test_data = test_data[["Number of times pregnant", "Plasma glucose conc", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)", "2-hour serum insulin (mu U/ml)","BMI (kg/m^2)", "Diabetes pedigree function","Age (yrs)"]] #this shows the list of variables/data columns that are in the training data sample


# In[5]:


print(training_data) #print training data sample, to check the headings, check that there is 80% of the data (looked at the [rows x columns] at the bottom)


# In[6]:


#Step 3: Create and train decision tree and random forest models
from sklearn.tree import DecisionTreeClassifier #importing a library
from sklearn.ensemble import RandomForestClassifier #importing a library
decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10) #creating the decision tree, with information that provides a seed number for the random generator, and the minimum number of samples needed before a node is 10, before a leaf splits  
random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10) #creating the random forest classifer, again with information that provides a seed number for the random generator, and the minimum number of samples needed before a node is 10, before a leaf splits
decision_tree_model.fit(training_data, training_label) #training the decision tree model with our training data and training label
random_forest_model.fit(training_data, training_label) #training the random forest model with our training data and training label


# In[7]:


#Step 4: Make predictions and evaluate the classification accuracy
from sklearn.metrics import accuracy_score #importing a library
y_pred_1 = decision_tree_model.predict(test_data) #applying the test data to the decision tree model, to determine the accuracy of the prediction model 
accuracy_1 = accuracy_score(test_label,y_pred_1) #determining the accuracy score against the column "Diabetes", using test data sample
y_pred_2 = random_forest_model.predict(test_data) #applying the test data to the random forest model, to determine the accuracy of the model 
accuracy_2 = accuracy_score(test_label,y_pred_2) #determining the confidence of the random forest model, using test data sample 

print(accuracy_1) #printing the accuracy score for the decision tree model 
print(accuracy_2) #printing the accuracy score for the random forest model 


# In[8]:


#Step 5: Visualize the decision tree in graphic format
estimator = random_forest_model.estimators_[7] #it pulls out one of the decision trees from the multitude of decision trees options in the random forest model 

from sklearn.tree import export_graphviz #importing library 

export_graphviz(estimator, out_file="tree.dot", 
                feature_names = ["Number of times pregnant", "Plasma glucose conc", "Diastolic BP (mm Hg)", "Triceps skin fold thickness (mm)", "2-hour serum insulin (mu U/ml)","BMI (kg/m^2)", "Diabetes pedigree function","Age (yrs)"],
                class_names = ["True", "False"],
                rounded = True, proportion = False,
                precision = 2, filled = True) #this is exporting the tree.dot file and describing the parameters/features of the visual for when it will be printed?

#a step not shown here is that I input into Windows cmd: dot -Tpng diabetestree.dot -o diabetestree.png -Gdpi=600. This step was to change the tree.dot file into a tree.png file

from IPython.display import Image #importing library to read image files (ex. .png)?


Image(filename = "diabetestree.png") #command to output an image file (.png)

