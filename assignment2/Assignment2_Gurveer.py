import os
import geopandas as gpd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from subprocess import check_call
import csv
import pandas as pd


def seagrass_function():
    # Get seagrass file path
    script_directory = os.path.dirname(__file__)
    relative_path = "seagrass/coastline_attr_seagrass.shp"
    absolute_file_path = os.path.join(script_directory, relative_path)

    # Task 1: Load the shapefile data using GeoPandas, show its top 10 records, and plot out the geographic data.
    coastline_attr = gpd.read_file(absolute_file_path)
    coastline_attr.head(10)
    coastline_attr.plot(figsize=(10, 8))

    # Task 2: Simple geospatial feature engineering
    coastline_attr["x"] = coastline_attr.geometry.x
    coastline_attr["y"] = coastline_attr.geometry.y

    # Task 3: Divide the data into 80% for training and 20% for testing
    training_data = coastline_attr.sample(frac=0.8, random_state=42)
    test_data = coastline_attr.drop(training_data.index)

    # Task 4: Prepare the training and test data
    training_label = training_data.pop("sea_grass")
    test_label = test_data.pop("sea_grass")
    training_data = training_data[
        ["salinity", "srtm30", "silicate", "phosphate", "disso2", "temp", "nitrate", "x", "y"]]
    test_data = test_data[["salinity", "srtm30", "silicate", "phosphate", "disso2", "temp", "nitrate", "x", "y"]]

    # Task 5: Create and train decision tree and random forest models
    decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
    random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
    decision_tree_model.fit(training_data, training_label)
    random_forest_model.fit(training_data, training_label)

    # Task 6: Make predictions and evaluate the classification accuracy
    y_pred_1 = decision_tree_model.predict(test_data)
    accuracy_1 = accuracy_score(test_label, y_pred_1)
    y_pred_2 = random_forest_model.predict(test_data)
    accuracy_2 = accuracy_score(test_label, y_pred_2)

    # Visualize the results
    print(accuracy_1)
    print(accuracy_2)

    # Task 7: Visualize the decision tree in graphic format
    # Pull out any one of the many decision trees – it doesn’t need to be the 6th.
    estimator = random_forest_model.estimators_[5]

    # Export as dot file
    export_graphviz(estimator, out_file="seagrass_tree.dot",
                    feature_names=["salinity", "srtm30", "silicate", "phosphate", "disso2", "temp", "nitrate", "x",
                                   "y"],
                    class_names=["True", "False"],
                    filled=True, proportion=False,
                    rounded=True, precision=2)

    # So… interesting twist here. I know this code works in principle, but I couldn't get it to run in my notebook. I
    # spent a good amount of time troubleshooting with Cooper, and we are in the same boat of confusion. HOWEVER,
    # we know it works because we successfully executed it in the command line. We may need to go over this together in
    # person. I’ll put the command line code below in case you’d like to experiment.

    check_call(["dot", "-Tpng", "seagrass_tree.dot", "-o", "seagrass_tree.png", "-Gdpi=600"])


def assignment_function():
    # Step 1: Read CSV data and convert to a pandas DataFrame.
    pima_data = []

    with open("pima-diabetes.csv", newline="") as csvfile:
        raw_pima_data = csv.reader(csvfile, delimiter=',')
        for row in raw_pima_data:
            pima_data.append(row)
    pima_data = pd.DataFrame(pima_data, columns=["NoP", "[PG]", "[DBP]", "TSFT", "2SI", "BMI", "DPF", "Age", "5YP"])

    # Step 2: Divide the data into 84% for training and 16% for testing
    training_data = pima_data.sample(frac=0.84, random_state=42)
    test_data = pima_data.drop(training_data.index)

    # Step 3: Prepare the training and test data
    training_label = training_data.pop("5YP")
    test_label = test_data.pop("5YP")

    # Step 4: Create and train decision tree and random forest models
    decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=10)
    random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=10)
    decision_tree_model.fit(training_data, training_label)
    random_forest_model.fit(training_data, training_label)

    # Step 5: Make predictions and evaluate the classification accuracy
    y_pred_1 = decision_tree_model.predict(test_data)
    accuracy_1 = accuracy_score(test_label, y_pred_1)
    y_pred_2 = random_forest_model.predict(test_data)
    accuracy_2 = accuracy_score(test_label, y_pred_2)

    # Visualize the results
    print(accuracy_1)
    print(accuracy_2)

    # Step 6: Visualize the decision tree in graphic format
    # Pull out any one of the many decision trees – it doesn’t need to be the 6th.
    estimator = random_forest_model.estimators_[3]

    export_graphviz(estimator, out_file="assignment2_tree.dot",
                    feature_names=["NoP", "[PG]", "[DBP]", "TSFT", "2SI", "BMI", "DPF", "Age"],
                    class_names=["True", "False"],
                    filled=True, proportion=False,
                    rounded=True, precision=2)

    check_call(["dot", "-Tpng", "assignment2_tree.dot", "-o", "assignment2_tree.png", "-Gdpi=600"])


def main():
    # seagrass_function()
    assignment_function()


if __name__ == "__main__":
    main()
