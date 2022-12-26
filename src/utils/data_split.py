# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

for dirname, _, filenames in os.walk('/content/drive/MyDrive/AI/WaterQualityProject/dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import warnings
warnings.filterwarnings('always')  

def data_split(df, test_size = 0.33):
    
    df["ph"].fillna(value = df["ph"].mean(), inplace = True)
    df["Sulfate"].fillna(value = df["Sulfate"].mean(), inplace = True)
    df["Trihalomethanes"].fillna(value = df["Trihalomethanes"].mean(), inplace = True)
    df.isnull().sum()

    X =  df.drop("Potability",axis=1).values
    y=   df['Potability'].values

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size, random_state=42)

    return X_train, X_test, y_train, y_test


