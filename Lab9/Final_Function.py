# @ Author : Anirudh Sathish 
# @ Roll_no : CS20B1125 

# Importing the neccesary libraries 
import pandas as pd 
import numpy as np 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestCentroid


# Reading the file 
df = pd.read_csv("diabetes.csv")


# The glucose , insulin and BMI features make sense 
#Let us talk about them 

# Getting all these values 
diabetes_related_data = df.iloc[:,[1,4,5]]
print(diabetes_related_data)

diabetes_output = df.iloc[:,[7]]
print(diabetes_output)
