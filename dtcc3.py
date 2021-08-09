Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import geopandas as gpd
>>> import pandas
>>> df=pandas.read_csv('C3.csv')
>>> training_data = df.sample(frac=0.85, random_state=42)
>>> test_data = df.drop(training_data.index)
>>> training_label = training_data.pop('priority_3')
>>> test_label = test_data.pop('priority_3')
>>> from sklearn.tree import DecisionTreeClassifier
>>> from sklearn.ensemble import RandomForestClassifier
>>> training_data = training_data[['sex','age_cat','marital_status','income_dec','highest_educat','house_size','current_student','per_mh','per_stress','per_weight','sense_belong','food_insecurity','smoke_status','alc_status','meds','regular_hcp','bmi_cat','PA','dis_count','adl_count','asthma','copd','arthritis','high_bp','high_chol','cvd','stroke','diabetes','cancer','mood_disorder','anxiety_disorder']]
>>> test_data = test_data[['sex','age_cat','marital_status','income_dec','highest_educat','house_size','current_student','per_mh','per_stress','per_weight','sense_belong','food_insecurity','smoke_status','alc_status','meds','regular_hcp','bmi_cat','PA','dis_count','adl_count','asthma','copd','arthritis','high_bp','high_chol','cvd','stroke','diabetes','cancer','mood_disorder','anxiety_disorder']]
>>> decision_tree_model = DecisionTreeClassifier(random_state=42, min_samples_leaf=100)
>>> random_forest_model = RandomForestClassifier(random_state=42, min_samples_leaf=100)
>>> decision_tree_model.fit(training_data, training_label)
DecisionTreeClassifier(min_samples_leaf=100, random_state=42)
>>> random_forest_model.fit(training_data, training_label)
RandomForestClassifier(min_samples_leaf=100, random_state=42)
>>> from sklearn.metrics import accuracy_score
>>> y_pred_1 = decision_tree_model.predict(test_data)
>>> accuracy_1 = accuracy_score(test_label,y_pred_1)
>>> y_pred_2 = random_forest_model.predict(test_data)
>>> accuracy_2 = accuracy_score(test_label,y_pred_2)
>>> print(accuracy_1)
0.5677777777777778
>>> print(accuracy_2)
0.6055555555555555
>>> 
