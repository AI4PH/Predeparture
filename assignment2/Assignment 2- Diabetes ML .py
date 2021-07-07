#!/usr/bin/env python
# coding: utf-8

# In[2]:


###Import all required libraries

import matplotlib
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from subprocess import check_call
import subprocess
from IPython.display import Image
import graphviz


# In[9]:


###Importing Pima Diabetes dataset

diabetes = pd.read_csv("pima-diabetes.csv")
diabetes.head()


# In[15]:


###Create testing and training data samples

train_data = diabetes.sample(frac=0.75,random_state=42)
test_data = diabetes.drop(train_data.index)


# In[16]:


len (train_data)


# In[17]:


len (test_data)


# In[18]:


###Prepare training and test data

train_label=train_data.pop("t2d")
test_label=test_data.pop("t2d")
train_data=train_data[["times_preg","glu","bp","skin_fold","serum_ins","bmi","dpf","age",]]
test_data=test_data[["times_preg","glu","bp","skin_fold","serum_ins","bmi","dpf","age",]]


# In[19]:


###Create decision tree and random forest plot

decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)


# In[20]:


decision_tree_model.fit(train_data, train_label)


# In[21]:


random_forest_model.fit(train_data, train_label)


# In[22]:


###Make predictions and test predictive accuracy

y_pred_1 = decision_tree_model.predict(test_data)
accuracy_1 = accuracy_score(test_label,y_pred_1)
y_pred_2 = random_forest_model.predict(test_data)
accuracy_2 = accuracy_score(test_label,y_pred_2)


# In[23]:


print (accuracy_1)


# In[24]:


print (accuracy_2)


# In[25]:


###Print image decision tree

from sklearn.tree import export_graphviz
estimator = random_forest_model.estimators_[5]
export_graphviz(estimator,
                out_file="tree.dot",
                feature_names=["times_preg","glu","bp","skin_fold","serum_ins","bmi","dpf","age"],
                class_names=["True","False"],
                rounded=True,
                proportion=False,
                precision=2,
                filled=True)


# In[26]:


from subprocess import check_call
import subprocess
subprocess.call(['dot', '-Tpng', 'tree.dot', '-o', 'Assignment_2_Diabetes_Tree.png', '-Gdpi=600'])

from IPython.display import Image
Image(filename="Assignment_2_Diabetes_Tree.png")


# In[1]:


###ANN

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


# In[3]:


t2d = loadtxt('pima-diabetes_nolab.csv', delimiter=',')


# In[4]:


# split into input (X) and output (y) variables
X = t2d[:,0:8]
y = t2d[:,8]


# In[6]:


# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[10]:


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[11]:


model.fit(X, y, epochs=150, batch_size=10)


# In[12]:


_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))


# In[14]:


# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-diabetes_nolab.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))


# In[16]:


# fit the keras model on the dataset without progress bars
model.fit(X, y, epochs=150, batch_size=10, verbose=0)
# evaluate the keras model
_, accuracy = model.evaluate(X, y, verbose=0)


# In[17]:


# make probability predictions with the model
predictions = model.predict(X)
# round predictions 
rounded = [round(x[0]) for x in predictions]


# In[21]:


# make class predictions with the model
predictions = model.predict_classes(X)


# In[22]:


# first neural network with keras make predictions
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-diabetes_nolab.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10, verbose=0)
# make class predictions with the model
predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

