#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:13:08 2021

@author: khandakerfoysalhaque
"""

import numpy as np

""" printing Arrays"""

a= np.array([1,2,3,4,5])
print(a)
print(a[4])


b=np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float)
print(b)

print(b.ndim)

print(b.shape)


c= np.zeros((3,4), dtype=np.complex)
print(c)



d=np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.complex)
print(d)