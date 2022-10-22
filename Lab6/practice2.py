# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 05:03:49 2022

@author: aniru
"""

import numpy as np 

np_array = np.ones([100,100])
print(np_array)

#print(dir(np))

#help(np.array)

x = np.array([1,2,3])
print(x)

grid = np.array([[4,5,6],[7,8,9]])
print(grid)
print(np.vstack([x,grid]))