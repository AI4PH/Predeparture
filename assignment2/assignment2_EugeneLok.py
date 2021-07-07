import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from subprocess import check_call
from sklearn.tree import export_graphviz
from IPython.display import Image 

# Load csv 
pimaDiabetesData = pd.read_csv("C:\\Users\\eugen\\Downloads\\pima-diabetes.csv",header = None)
print(pimaDiabetesData)

# Divide data in 80% for training and 20% for testing 
trainingData = pimaDiabetesData.sample(frac=0.8, random_state=42)
testData = pimaDiabetesData.drop(trainingData.index)
print(trainingData)

# Get labels from training data 
trainLabel = trainingData.pop(8)
testLabel = testData.pop(8)

# Prepare test and training data 
decisionTreeModel = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
randomForestModel = RandomForestClassifier(random_state=42, min_samples_leaf=10)
decisionTreeModel.fit(trainingData, trainLabel)
randomForestModel.fit(trainingData, trainLabel)

# Calculate and Print Classification accuracy
y_pred_1 = decisionTreeModel.predict(testData)
accuracy_1 = accuracy_score(testLabel,y_pred_1)
print(accuracy_1)
y_pred_2 = randomForestModel.predict(testData)
accuracy_2 = accuracy_score(testLabel,y_pred_2)
print(accuracy_2)

# Visualize 2nd decision tree
estimator = randomForestModel.estimators_[1]

# # Export as dot file
export_graphviz(estimator, out_file='tree.dot', 
                feature_names = ["TIMES_PREGNANT","2H_GLUCOSE","DIASTOLIC_BP","TRICEPS_SKIN_THICKNESS","2H_INSULIN","BMI","DIABETES_PEDIGREE","AGE"],
                class_names = ["True", "False"],
                rounded = True, proportion = False, 
                precision = 2, filled = True)

check_call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

# Display in jupyter notebook
Image(filename = 'tree.png')