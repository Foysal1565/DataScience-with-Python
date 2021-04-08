#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 01:21:01 2021

@author: khandakerfoysalhaque
"""

""" numpy examples """

import numpy as np 

import pandas as pd


array= [1,2,3,4,5,6]
print(array)


order=range(1,7,1)
print(pd.Series(array, index=order))


"""changing the index"""

a= pd.Series(array, index=order)
print(a)

a.index = ['A','B','C','D','E','F']

print(a[:-3])

array1=range(1,10,2)
array2=range(1,5,1)

s1=pd.Series(array1)

s2=pd.Series(array2)

print(s1)
print(s2)

s3=  s1.add(s2)
print (s3)


s4=  s1.mul(s2)
print (s4)

s5=  s1.div(s2)
print (s5)

print('The median of s1 is', s1.median())
print('The median of s2 is', s2.median())


print('The max of s1 is', s1.max())
print('The max of s2 is', s2.max())



print('The min of s1 is', s1.min())
print('The min of s2 is', s2.min())


""" creating data frame with pd """

df1=pd.DataFrame(np.random.randn(5,5), index=range(1,6,1), columns=['A','B','C','D','E'])
print(df1)

#printing head or tail 
print(df1.head(2))

print(df1.tail(2))

#Sorting values
print(df1[1:4])
print(df1.sort_values(by='A')[2:5])


print(df1.iloc[1:4])


""" Saving and reading DataFrame from csv"""

df1.to_csv('df1.csv')

x=pd.read_csv('df1.csv')
print(x.head(3))

df1.to_excel('df1.xlsx', sheet_name='sheet1')

y=pd.read_excel('df1.xlsx', 'sheet1')
print(y.head(1))






















