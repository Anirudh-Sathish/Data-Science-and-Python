# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:16:11 2022

@author: aniru
"""

# Defining the library 
import pandas as pd 

import numpy as np 

s1 = pd.Series([1,2,3])
print(s1)



'''
s1 = pd.Series([1,2,3])
print(s1)
print(type(s1))

n1 = np.array([5,6,7])
s2 = pd.Series(n1)
print(s2)
print(type(s2))

n2 = np.random.rand(5)
s3 = pd.Series(n2)
print(s3)
print(type(s3))

s4 = pd.Series(10,[1,2,3,4])
print(s4)
print(type(s4))

s5 = pd.Series(['a','b','c','d'],[1,2,3,4])
print(s5)
print(type(s5))

s6 = pd.Series([10,20,30])
s7 = pd.Series([120,25,35])
print(s6+s7)
print(s6-s7)
print(s6*s7)
print(s6/s7)


s6 = pd.Series([10,20,30,40,50,60])
print(s6)
print("First value:",s6[0])
print("First 2 values:\n",s6.head(2))
print("Last 2 values:\n",s6.tail(2))
#Slicing
print("Second and third values:\n",s6[1:3])
print("Second to fifth values:\n",s6[1:5])
#Location loc
print("First 4 values:\n",s6[0:4])
print("First 5 values:\n",s6.loc[:4])
print("3 values:\n",s6.loc[2:4])
'''