#Assignment 2: Building your own decision tree and random forest models to predict the existence of seagrass
In this exercise, you will build your own decision tree and random forest models to complete a task very similar to what we have demoed in the class. You will work on the same dataset, but your goal will be to predict the existence of seagrass (a classification problem), rather than to predict the concentration of nitrate as in our demo.

(Credit: The exercise dataset is revised based on a workshop organized by Dr. Yingjie Hu, which is in turn based on the tutorial here:
https://learn.arcgis.com/en/projects/predict-seagrass-habitats-with-machine-learning/)

##Task 1: Load the shapefile data using GeoPandas, show its top 10 records, and plot out the geographic data.
```import geopandas as gpd
coastline_attr = gpd.read_file("!!!path to the shp file!!!")
coastline_attr.head(10)
coastline_attr.plot(figsize=(10,8))
```
##Task 2: Simple geospatial feature engineering
```coastline_attr["x"] = coastline_attr.geometry.x
coastline_attr["y"] = coastline_attr.geometry.y
```

##Task 3: Divide the data into 80% for training and 20% for testing
```training_data = coastline_attr.sample(frac=0.8, random_state=42)
test_data = coastline_attr.drop(training_data.index)
```

##Task 4: Prepare the training and test data
```training_label = training_data.pop("sea_grass")
test_label = test_data.pop("sea_grass")
training_data = training_data[["salinity","srtm30","silicate","phosphate","disso2","temp","nitrate",”x”, "y"]]
test_data = test_data[["salinity","srtm30","silicate","phosphate","disso2","temp","nitrate","x","y"]]
```

##Task 5: Create and train decision tree and random forest models
```from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
decision_tree_model.fit(training_data, training_label)
random_forest_model.fit(training_data, training_label)
```

##Task 6: Make predictions and evaluate the classification accuracy
```from sklearn.metrics import accuracy_score
y_pred_1 = decision_tree_model.predict(test_data)
accuracy_1 = accuracy_score(test_label,y_pred_1)
y_pred_2 = random_forest_model.predict(test_data)
accuracy_2 = accuracy_score(test_label,y_pred_2)


#visualize the results
print(accuracy_1)
print(accuracy_2)
```

##Task 7: Visualize the decision tree in graphic format
```#pull out any one of the many decision trees – it doesn’t need to be the 6th.
estimator = random_forest_model.estimators_[5]

from sklearn.tree import export_graphviz

# Export as dot file
export_graphviz(estimator, out_file='tree.dot', 
                feature_names = ["salinity","srtm30","silicate","phosphate","disso2","temp","nitrate","x", "y"],
                class_names = ["True", "False"],
                rounded = True, proportion = False, 
                precision = 2, filled = True)

#So… interesting twist here. I know this code works in principle, but I couldn’t get it to run in my notebook. I spent a good amount of time troubleshooting with Cooper, and we are in the same boat of confusion. HOWEVER, we know it works because we successfully executed it in the command line. We may need to go over this together in person. I’ll put the command line code below in case you’d like to experiment. 

from subprocess import check_call

check_call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

# Display in jupyter notebook
Image(filename = 'tree.png')

#If you’d like to try running this in command line, first make sure that the graphviz folder is in your system’s environment variables. Make sure your working directory (the directory at the left when you run the command line) is where your dot file was created. Then you can run the following command without the pound sign: 
#dot -Tpng tree.dot -o tree.png
#This will create a png file in your working directory that you can open up and explore.
```

#Assignment
OK, so now you have trained a decision tree on the presence of seagrass. Spend some time thinking about what your model shows, and how you might interpret the results. For the assignment itself, all I’m asking you to do is create another random forest model for a different dataset. So, you will need to rewrite large parts of your script, but you won’t necessarily need to rewrite it from scratch. 
The new dataset is a public health dataset representing the Pima Native American people in Arizona, US, and specifically, 8 health measurements plus an indication whether they had an onset of diabetes within 5 years of the study. The 8 variables (health-related measurements) are:
1. Number of times pregnant
2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3. Diastolic blood pressure (mm Hg)
4. Triceps skin fold thickness (mm)
5. 2-Hour serum insulin (mu U/ml)
6. Body mass index (weight in kg/(height in m)^2)
7. Diabetes pedigree function
8. Age (years)
As mentioned above, there is a 9th column representing 0s and 1s: whether the individual had diabetes after 5 years.
Your task is to simply create a random forest model from this dataset. You can feel free to visualize the model just like we did above, but there isn’t a strict requirement for it. 
Some important notes:
1.	Since this dataset does not have spatial information, you can skip many of the processing steps from above. 
2.	Here is the documentation for reading a CSV file in Python: https://docs.python.org/3/library/csv.html. Basically, you will use a “with open” function like this:
```import csv
with open(‘pima-diabetes.csv’, newline=’’) as csvfile:
   pima_data = csv.reader(csvfile, delimiter=',')
```
And the rest is up to you! 😊
3.	If this is all too easy for you, or you’d like to explore another machine learning approach, I suggest learning how to work through artificial neural networks. Learning how to train a neural net is no simple matter, either conceptually or technically, but there are some really great walkthroughs using techs and data that you already have. Here’s one that works particularly well: https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

If you decide to work through this tutorial, I can help you if you run into issues. Keep in mind that if you’ve installed TensorFlow, you’ve also already installed Keras, and you would access all Keras modules through tensorflow.keras (i.e., to access Sequential, you would type: 
```from tensorflow.keras.models import Sequential
```


