Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df=pandas.read_csv('C3.csv')
>>> plt.subplots(figsize=(20,15))
(<Figure size 2000x1500 with 1 Axes>, <AxesSubplot:>)
>>> sns.heatmap(df.corr(), annot = True)
<AxesSubplot:>
>>> plt.show()
