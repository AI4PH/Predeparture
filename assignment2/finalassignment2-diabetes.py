Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import geopandas as gdp
>>> import pandas
>>> import csv
>>> data=[]
>>> with open('pima-diabetes.csv',newline='') as csvfile:
	pima_data=csv.reader(csvfile, delimiter=',')
	for row in pima_data:
		data.append(row)

>>> headerlist=['pregnant','glucose','BP','skinfold','insulin','BMI','diabetesped','age','diab']
>>> dia=pandas.read_csv('pima-diabetes.csv',names=headerlist)
# adding the header list was the most ~creative~ I could manage to be with my python profeciency level

>>> dia.head(10)
   pregnant  glucose  BP  skinfold  insulin   BMI  diabetesped  age  diab
0         6      148  72        35        0  33.6        0.627   50     1
1         1       85  66        29        0  26.6        0.351   31     0
2         8      183  64         0        0  23.3        0.672   32     1
3         1       89  66        23       94  28.1        0.167   21     0
4         0      137  40        35      168  43.1        2.288   33     1
5         5      116  74         0        0  25.6        0.201   30     0
6         3       78  50        32       88  31.0        0.248   26     1
7        10      115   0         0        0  35.3        0.134   29     0
8         2      197  70        45      543  30.5        0.158   53     1
9         8      125  96         0        0   0.0        0.232   54     1
>>> training_data = dia.sample(frac=0.85, random_state=42)
>>> test_data = dia.drop(training_data.index)
>>> training_label = training_data.pop('diab')
>>> test_label = test_data.pop('diab')
>>> from sklearn.tree import DecisionTreeClassifier
>>> from sklearn.ensemble import RandomForestClassifier
>>> decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
>>> random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
>>> decision_tree_model.fit(training_data, training_label)
DecisionTreeClassifier(min_samples_leaf=10, random_state=42)
>>> random_forest_model.fit(training_data, training_label)
RandomForestClassifier(min_samples_leaf=10, random_state=42)
>>> from sklearn.metrics import accuracy_score
>>> y_pred_1 = decision_tree_model.predict(test_data)
>>> accuracy_1 = accuracy_score(test_label,y_pred_1)
>>> y_pred_2 = random_forest_model.predict(test_data)
>>> accuracy_2 = accuracy_score(test_label,y_pred_2)
>>> print(accuracy_1)
0.7739130434782608
>>> print(accuracy_2)
0.7652173913043478
>>> # 77.39% and 76.52% accuracy
>>> # at 85% data delegated to training and 15% data delegated to testing
>>> from sklearn.tree import export_graphviz
>>> estimator = random_forest_model.estimators_[5]
>>> export_graphviz(estimator, out_file='tree.dot',
		feature_names = ['pregnant','glucose','BP','skinfold','insulin','BMI','diabetesped','age'],
		class_names = ["True", "False"],
		rounded = True, proportion = False,
		precision = 2, filled = True)
>>> from subprocess import check_call
>>> check_call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
Traceback (most recent call last):

>>> # The last line of code was not executable for me "FileNotFoundError: [Errno 2] No such file or directory: 'dot'"
>>> dot-Tpng tree.dot -o tree.png
SyntaxError: invalid syntax
>>> # I tried to fix it, but I'm working in IDLE anyways so I cant see the graph right now anyways so I am satisfied with just knowing the accuracy percentages
