import pandas

from IPython.display import Image
from numpy.random import RandomState

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from subprocess import check_call
from sklearn.tree import export_graphviz

# read diabetes data from csv file
diabetesData = pandas.read_csv("C:/Users/alhed/Documents/ai4ph/assignment2/pima-diabetes.csv")

# divide data into 80% training data and 20% testing data
training_data = diabetesData.sample(frac=0.8, random_state=42)
test_data = diabetesData.loc[~diabetesData.index.isin(training_data.index)]
training_label = training_data.pop("D5Y") # D5Y = diabetes after 5 years 
test_label = test_data.pop("D5Y")

# prepare the training and test data
# TP = # of times pregnant, PGC = plasma glucose concentration, DBP = diastolic blood pressure (mm Hg)
# TST = triceps skin fold thickness (mm), 2SI = 2-hour serum insulin (mu U/mL), 
# BMI = body mass index (weight in kg/(height in m)^2), DPF = diabetes pedigree function, AGE = age (years)
training_data = training_data[["TP","PGC","DBP","TST","2SI","BMI","DPF","AGE"]]
test_data = test_data[["TP","PGC","DBP","TST","2SI","BMI","DPF","AGE"]]

# create and train decision tree and random forest models
decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
decision_tree_model.fit(training_data, training_label)
random_forest_model.fit(training_data, training_label)

# make predictions ad evaluate the classification accuracy
y_pred_1 = decision_tree_model.predict(test_data)
accuracy_1 = accuracy_score(test_label,y_pred_1)
y_pred_2 = random_forest_model.predict(test_data)
accuracy_2 = accuracy_score(test_label,y_pred_2)

#visualize the results
print(accuracy_1)
print(accuracy_2)

## visualize the decision tree as a graph
# pull out one of the decision trees
estimator = random_forest_model.estimators_[5]

# Export as dot file
export_graphviz(estimator, out_file='tree.dot', 
                feature_names = ["TP","PGC","DBP","TST","2SI","BMI","DPF","AGE"],
                class_names = ["True", "False"],
                rounded = True, proportion = False, 
                precision = 2, filled = True)

# converts dot file to png file
check_call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

# display in jupyter notebook
Image(filename = 'tree.png')