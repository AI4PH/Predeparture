import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from subprocess import check_call
from IPython.display import Image

#Set header titles
FILE_HEADER = ['times_pregnant', 'glucose', 'diastolic', 'tricep_skin_fold_thickness', 'insulin', 'BMI', 'diabetes_pedigree_function', 'age', 'diabetes']

#Open CSV files
with open('pima-diabetes.csv', newline='') as csvfile:   
    pima_data = pd.read_csv(csvfile, delimiter=',', header=None,
    names=FILE_HEADER)

#Split data into 80% training data, 20% testing data
training_data = pima_data.sample(frac=0.8, random_state=42)
test_data = pima_data.drop(training_data.index)

#Split answers from dataset
training_label = training_data.pop("diabetes")
test_label = test_data.pop("diabetes")
training_data = training_data[['times_pregnant', 'glucose', 'diastolic', 'tricep_skin_fold_thickness', 'insulin', 'BMI', 'diabetes_pedigree_function', 'age']]
test_data = test_data[['times_pregnant', 'glucose', 'diastolic', 'tricep_skin_fold_thickness', 'insulin', 'BMI', 'diabetes_pedigree_function', 'age']]

#Create a decision tree and random forest model
decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
decision_tree_model.fit(training_data, training_label)
random_forest_model.fit(training_data, training_label)

#Check accuracy
y_pred_1 = decision_tree_model.predict(test_data)
accuracy_1 = accuracy_score(test_label,y_pred_1)
y_pred_2 = random_forest_model.predict(test_data)
accuracy_2 = accuracy_score(test_label,y_pred_2)


#visualize the results
print(accuracy_1)
print(accuracy_2)

# Pull out any one of the many decision trees – it doesn’t need to be the 6th.
estimator = random_forest_model.estimators_[3]

# Export as dot file
export_graphviz(estimator, out_file='shanna_tree.dot',                 
        feature_names = ['times_pregnant', 'glucose', 'diastolic', 'tricep_skin_fold_thickness', 'insulin', 'BMI', 'diabetes_pedigree_function', 'age'],                
        class_names = ["True", "False"],                
        rounded = True, proportion = False,                 
        precision = 2, 
        filled = True)

check_call(['dot', '-Tpng', 'shanna_tree.dot', '-o', 'shanna_tree.png', '-Gdpi=600'])

# Display in jupyter notebook
Image(filename = 'shanna_tree.png')
