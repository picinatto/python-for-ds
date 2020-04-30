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


# Multi level INDEXES in DataFrames

# Setting up the data
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
# Create a list of pairs
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Create a dataframe from random numbers
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df) # Creates a two level index, the G1 and G2 and the 1,2,3

# We can get data using the outer index
print(df.loc['G1'])

# Or we can get the subindex, for the example the first row of G1
print(df.loc['G1'].loc[1])

# To name the indexes
df.index.names = ['Groups','Numbers']
print(df)

# To get a specific value
print(df.loc['G2'].loc[2]['B'])

# To select a section we can also use cross section G1
print(df.xs('G1')) # The same as print(df.loc['G1'])

# The cross section can skip the outermost index
# To get the all numbers 1 rows, regardless of the Group
print(df.xs(1,level='Numbers'))