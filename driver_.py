# # -*- coding: utf-8 -*-
# """DRIVER_.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1f6zE3bov4RmTEBiYEXlbXOs5OqEqNbEV
# """

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('ddF.csv')
# X = df.iloc[:, [0,1,4,8,9]].values
# y = df.iloc[:, 2].values
# df.tail()

# # corr = df.corr()
# # ax1 = sns.heatmap(corr, cbar=0, linewidths=2,vmax=1, vmin=0, square=True, cmap='Blues')
# # plt.show()

# # df.info()

# df.shape

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
# # print(X[1])





# # print(X_train[1])

# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)

# temp = list(regressor.coef_)
# # temp.append(regressor.predict([[0,0,0,0,0]])[0])

# print(*temp)

# -*- coding: utf-8 -*-
"""DRIVER_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f6zE3bov4RmTEBiYEXlbXOs5OqEqNbEV
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ddF.csv')
X = df.iloc[:, 0:5].values
y = df.iloc[:, -1].values
df.tail()

# corr = df.corr()
# ax1 = sns.heatmap(corr, cbar=0, linewidths=2,vmax=1, vmin=0, square=True, cmap='Blues',annot=True)
# plt.show()

# df.info()

df.shape

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
# print(X[1])





# print(X_train[1])

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

regressor.coef_

# print(regressor.predict([[0,0,0,0,0]]))

# print(regressor.predict([[52,1305,24500,30,43]]))

temp = list(regressor.coef_)
temp.append(regressor.predict([[0,0,0,0,0]])[0])

print(*temp)