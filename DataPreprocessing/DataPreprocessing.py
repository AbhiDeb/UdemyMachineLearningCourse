#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 01:47:37 2017

@author: Abhitesh Debnath
"""
#%%
#==============================================================================
# Importing Libraries
#==============================================================================
#Mathematical Librarimpy
import numpy as np
#To Plot charts
import matplotlib.pyplot as plt
#To import and manage datasets
import pandas as pd

#==============================================================================
# Importing Dataset
#==============================================================================
dataset = pd.read_csv('Data.csv')

#Making matrix of independent variables
#i.e columns Country,Age,Salary
X = dataset.iloc[: , :-1].values
# : means all rows and all columns. :-1 means all rows except last one

#Making vector of dependent variable, i.e. Last Column
Y = dataset.iloc[:,3].values

#Z = dataset.iloc[:,2].values

#==============================================================================
# Handling missing data
#==============================================================================
#Calculate mean and replace the data with it's mean
#Importing Libraries of Python to do that job
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
#Missing Values, that represent those missing values in data set
#Straetgy, that we are using
#axis, to fit it in the dataset along the column

#Not going to fit all the columns, just 1 and 2(3 is taken because it ignores the upper bound)
imputer = imputer.fit(X[:, 1:3])
#To fit imputer into object X
#Replacing missing data in X using imputer
X[:,1:3] = imputer.transform(X[:,1:3])

#==============================================================================
# Encoding Categorical Data
#==============================================================================
#For info refer Notes.txt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
#To tell onhotencoder to take only 0th column for making dummy variables
X = onehotencoder.fit_transform(X).toarray()
#For Y we don't have to use Dummy Variable as it has only 2 values Yes/No
#So we are only going to use LabelEncoder for that
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

#==============================================================================
# Splitting the dataset into training set and test set
#==============================================================================
from sklearn.cross_validation import train_test_split
#Now we will make 4 matrix for our 2 splitted datasets
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#==============================================================================
#Feature Scaling
#==============================================================================
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
#Since we already fit_transform sc_X, we will only use transform for next use
X_test = sc_X.transform(X_test)