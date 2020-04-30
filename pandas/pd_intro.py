import numpy as np
import pandas as pd

# Setting up data
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

''' 

    SERIES

'''
print('\n*************\nSeries in Pandas\n*************\n')
#Setting the PD Series
print(pd.Series(data=my_data))

# Using a custom index
print(pd.Series(data=my_data,index=labels))

# Create a series passing a numpy array
print(pd.Series(arr))

# Setting an series from a dict, pandas will automatically set
#   the keys to index and the values to rows
print(pd.Series(d))

# Panda Series can hold not only numbers, can hold a variety of data types
print(pd.Series(data=labels))

# Using the index
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

# To get value for one element, use [] and the label
print(ser1['USA'])

# When we add two series, it will try to find the values that are in the 2
#   and the ones not found in the two will be null
print(ser1 + ser2)