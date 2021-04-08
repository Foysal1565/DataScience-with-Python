#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:01:35 2021

@author: khandakerfoysalhaque
"""

from scipy import constants
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
""" printing constants """

print(constants.g)

print('planks constant', constants.h)

""" Creating Dataframe """

df = pd.DataFrame(np.random.randn(6,5), columns=('apple','ball','cat','dog', 'Egg'), index=('a','b','c','d','e','f'))
print(df)
#create a by b matrix

#np.random.seed(10)

N=30

x= np.random.randn(N)

y= np.random.randn(N)

area= (30 * np.random.randn(N))**2
colors=np.random.randn(N)

""" Scatter and bar plot """

plt.scatter(x, y, s=area, c=colors, alpha=0.4)

from matplotlib import style
style.use('ggplot')

x=[1, 5, 10, 15]
y=[1, 2, 3, 4]

plt.bar(x, y, color='r', align='center')
plt.show()


""" Printing array with range """

g= np.random.rand(5)
print(g)

f=list(range(1, -10, -1))
print(f)

for i in frange(1,10,1):
    print(i)
    
""" Printing array with floating number"""

import numpy as np
for i in np.arange(1, 5, 0.5):
    print(i)
    
    
    
