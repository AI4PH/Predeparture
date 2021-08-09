Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
import 
>>> import numpy as np
>>> import sklearn
>>> from sklearn.cluster import KMeans
>>> from sklearn.preprocessing import LabelEncoder
>>> from sklearn.preprocessing import MinMaxScaler
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> train = pd.read_csv('MD.csv')
>>> test = pd.read_csv('MD.csv')
>>> print(train.head())
   ADM_RNO  health_region  sex  ...          X          Y  priority_score
0     1283          48935    1  ...  35.169907 -16.505440               3
1     4074          24909    1  ...  34.918760 -14.077579               3
2     4341          35937    1  ...  33.926470  -9.938154               3
3     6767          24912    2  ...  34.811374 -14.488888               3
4     7487          48933    1  ...  34.796954 -14.422882               2

[5 rows x 27 columns]
>>> print("\n")


>>> print(test.head())
   ADM_RNO  health_region  sex  ...          X          Y  priority_score
0     1283          48935    1  ...  35.169907 -16.505440               3
1     4074          24909    1  ...  34.918760 -14.077579               3
2     4341          35937    1  ...  33.926470  -9.938154               3
3     6767          24912    2  ...  34.811374 -14.488888               3
4     7487          48933    1  ...  34.796954 -14.422882               2

[5 rows x 27 columns]
>>> print(train.columns.values)
['ADM_RNO' 'health_region' 'sex' 'age_cat' 'sexuality' 'income_dec'
 'highest_educat' 'food_insecurity' 'smoke_status' 'alc_status' 'bmi_cat'
 'PA' 'dis_count' 'adl_count' 'asthma' 'copd' 'arthritis' 'high_bp' 'cvd'
 'diabetes' 'cancer' 'mood_disorder' 'anxiety_disorder' 'HospitalDist' 'X'
 'Y' 'priority_score']
>>> train.isna().head()
   ADM_RNO  health_region    sex  ...      X      Y  priority_score
0    False          False  False  ...  False  False           False
1    False          False  False  ...  False  False           False
2    False          False  False  ...  False  False           False
3    False          False  False  ...  False  False           False
4    False          False  False  ...  False  False           False

[5 rows x 27 columns]
>>> test.isna().head()
   ADM_RNO  health_region    sex  ...      X      Y  priority_score
0    False          False  False  ...  False  False           False
1    False          False  False  ...  False  False           False
2    False          False  False  ...  False  False           False
3    False          False  False  ...  False  False           False
4    False          False  False  ...  False  False           False

[5 rows x 27 columns]
>>> print(train.isna().sum())
ADM_RNO             0
health_region       0
sex                 0
age_cat             0
sexuality           0
income_dec          0
highest_educat      0
food_insecurity     0
smoke_status        0
alc_status          0
bmi_cat             0
PA                  0
dis_count           0
adl_count           0
asthma              0
copd                0
arthritis           0
high_bp             0
cvd                 0
diabetes            0
cancer              0
mood_disorder       0
anxiety_disorder    0
HospitalDist        0
X                   0
Y                   0
priority_score      0
dtype: int64
>>> print("\n")


>>> print(test.isna().sum())
ADM_RNO             0
health_region       0
sex                 0
age_cat             0
sexuality           0
income_dec          0
highest_educat      0
food_insecurity     0
smoke_status        0
alc_status          0
bmi_cat             0
PA                  0
dis_count           0
adl_count           0
asthma              0
copd                0
arthritis           0
high_bp             0
cvd                 0
diabetes            0
cancer              0
mood_disorder       0
anxiety_disorder    0
HospitalDist        0
X                   0
Y                   0
priority_score      0
dtype: int64
>>> train.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 27 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   ADM_RNO           1000 non-null   int64  
 1   health_region     1000 non-null   int64  
 2   sex               1000 non-null   int64  
 3   age_cat           1000 non-null   int64  
 4   sexuality         1000 non-null   int64  
 5   income_dec        1000 non-null   int64  
 6   highest_educat    1000 non-null   int64  
 7   food_insecurity   1000 non-null   int64  
 8   smoke_status      1000 non-null   int64  
 9   alc_status        1000 non-null   int64  
 10  bmi_cat           1000 non-null   int64  
 11  PA                1000 non-null   int64  
 12  dis_count         1000 non-null   int64  
 13  adl_count         1000 non-null   int64  
 14  asthma            1000 non-null   int64  
 15  copd              1000 non-null   int64  
 16  arthritis         1000 non-null   int64  
 17  high_bp           1000 non-null   int64  
 18  cvd               1000 non-null   int64  
 19  diabetes          1000 non-null   int64  
 20  cancer            1000 non-null   int64  
 21  mood_disorder     1000 non-null   int64  
 22  anxiety_disorder  1000 non-null   int64  
 23  HospitalDist      1000 non-null   int64  
 24  X                 1000 non-null   float64
 25  Y                 1000 non-null   float64
 26  priority_score    1000 non-null   int64  
dtypes: float64(2), int64(25)
memory usage: 211.1 KB
>>> train = train.drop(['X','Y'], axis=1)
>>> test = test.drop(['X','Y'], axis=1)
>>> kmeans = KMeans(n_clusters=2)
>>> X = np.array(train.drop(['priority_score'], 1).astype(float))
>>> Y = np.array(train['priority_score'])
>>> kmeans.fit(X)
KMeans(n_clusters=2)
>>> for i in range(len(X)):
	predict_me = np.array(X[i].astype(float))
	predict_me = predict_me.reshape(-1, len(predict_me))
	prediction = kmeans.predict(predict_me)
	if prediction[0] == Y[i]:
		correct += 1

		
>>> print(correct/len(X))
0.105
>>> kmeans = kmeans = KMeans(n_clusters=2, max_iter=600, algorithm = 'auto')
>>> kmeans.fit(X)
KMeans(max_iter=600, n_clusters=2)
>>> correct = 0
>>> for i in range(len(X)):
	predict_me = np.array(X[i].astype(float))
	predict_me = predict_me.reshape(-1, len(predict_me))
	prediction = kmeans.predict(predict_me)
	if prediction[0] == Y[i]:
		correct += 1

		
>>> print(correct/len(X))
0.123
>>> scaler = MinMaxScaler()
>>> X_scaled = scaler.fit_transform(X)
>>> kmeans.fit(X_scaled)
KMeans(max_iter=600, n_clusters=2)
>>> correct = 0
>>> for i in range(len(X)):
	predict_me = np.array(X[i].astype(float))
	predict_me = predict_me.reshape(-1, len(predict_me))
	prediction = kmeans.predict(predict_me)
	if prediction[0] == Y[i]:
		correct += 1

		
>>> print(correct/len(X))
0.007
>>> 
