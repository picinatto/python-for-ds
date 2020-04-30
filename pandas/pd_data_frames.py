import numpy as np
import pandas as pd
from numpy.random import randn

''' 

    DATA FRAMES 

'''
print('\n*************\nData Frames in Pandas\n*************\n')

# Adjusting the random method to get the same results from the lecture
np.random.seed(101)

# Creating a data frame
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

# Getting value from a data frame

# Getting all rows from the 'W' column
print('\n*************\nGetting values in Pandas Data Frames\n*************\n')
print(df['W']) # it becomes a series

# If wanted several columns, pass a list of columns
print(df[['W','Z']]) # get back a data frame

# Creating a new column
df['new'] = df['W'] + df['Y']
print(df)

# Droping a column use drop and axis=1, to persist the drop in original DF, use inplace=True
df.drop('new',axis=1,inplace=True)
print(df)

# Droping a row use drop and axis=0, to persist the drop in original DF, use inplace=True
df.drop('E',axis=0,inplace=True)
print(df)

# Pandas dataframes are fancy 2d numpy arrays
print(str(df.shape)) #4 rows and 4 columns

# Selecting rows, there are two methods

# Using Loc for label finding
print(df.loc['D']) # Return a series of the values for each column

# Using iloc for index base location
print(df.iloc[3])

# Selecting the subset of rows and columns
print(df.loc['B','Y'])

# Selecting subset of rows
print(df.loc[['A','B'],['W','Y']])

# Conditional selection with data frames
print(df[df>0])

# To remove rows that are false from the dataframe
print(df[df['W']>0])

# Call commands in a filtered DF
bool_df = df['W']>0
filtered_df = df[bool_df]
print(filtered_df['X'])

# The same as writing all in one line..
print(df[df['W']>0]['X'])

# To use multiple conditions use '&', do not use 'and' for 'or' use '|'
print(df[(df['W']>0) & (df['Y']>0)])



# INDEX IN DATA FRAMES

print('\n*************\nWorking with index Pandas Data Frames\n*************\n')

# To reset indexes, the old index is moved to a index column
# Needs inplace to persist
print(df.reset_index())

new_index = 'CA NY WY OR'.split()
df['States'] = new_index
print(df)

# To set a column to be the index, use setindex
print(df.set_index(df['States']))