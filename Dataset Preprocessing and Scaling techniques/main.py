import pandas as pd
from sklearn import preprocessing
import numpy as np

# task1
# file = pd.read_csv('employee.csv')
# df = pd.DataFrame(file)
# df["Gender"].fillna("No Gender", inplace=True)
# print(df["Gender"].head(20))

# task2

# dict = {
#     "age": [25, 36, 30, 27, 38, 42, 34],
#     "salary": [42000, 50000, 45000, 43000, 51000, 62000, 48000],
# }
# df = pd.DataFrame(dict)
# print(df.head())
# x = np.array([dict["age"], dict["salary"]])
# scaling = preprocessing.MinMaxScaler()
# print(scaling.fit_transform(df.head()))

#task 3

dict = {
    "age": [25, 36, 30, 27, 38, 42, 34],
    "salary": [42000, 50000, 45000, 43000, 51000, 62000, 48000],
}
df = pd.DataFrame(dict)
print(df.head())
scaling = preprocessing.StandardScaler()
print(scaling.fit_transform(df.head()))

#task4

# dict = {'First Score': [100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score': [np.nan, 40, 80, 98]}
#
# df = pd.DataFrame(dict)
# print(df.interpolate(method='linear', limit_direction='backward'))