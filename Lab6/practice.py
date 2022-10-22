# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:52:28 2022

@author: aniru
"""

import pandas as pd

list_1 = [1,2,3,4,5]
print(list_1)

Series_1 = pd.Series(list_1)
print("First 2 values ",Series_1.head())

list_2 = ["Ram","Shyam","Teddy","Rhesus","Monkey"]

dict_r = {"name":list_2,"num":list_1}

df1 = pd.DataFrame(dict_r)
#print(df1)
#print(df1.info)

df2 = df1 # Shallow copy
#print(df2)

df3 = df1.copy(deep = "true")
#print(df3)


print(df1)
print(df2.iat[3,0])

print(df2.dtypes)

s4 = pd.Series(999,[1,2,3,4])
print(s4)

print(df2)
df4 = df2.rename(columns = {'name':'Monkey','num':'Integers'})
print(df4)

df4 = df4.rename(columns = {'Monkey':'Vijay','Integers':'Kargil'})
print(df4)

print(df1.loc[0:1])

df5 = pd.DataFrame([["Sha","RSA"],["Python","Qiskit"]],columns =["Crypto","Prim"])
print(df5)

print(df1)
df6 = df1.append(df5)
print(df6)

df7= pd.concat([df1,df5])
print(df7)