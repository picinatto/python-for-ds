import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

# Find all the unique values in a columns
print(df['col2'].unique()) # Returns an array

# Return the number of unique values
print(df['col2'].nunique())

# To return how many times echa value ocurrs
print(df['col2'].value_counts())

###
### SELECTING DATA
###

print(df[(df['col1']>2) & (df['col2']==444)])

# Applying custom funcitons to the DF

# Creating the function
def times2(x):
    return x*2

# Using apply
print(df['col1'].apply(times2))

# using apply in built in functions
print(df['col3'].apply(len))

# using lambdas
print(df['col2'].apply(lambda x: x*2))


# REMOVING COLUMNS
print(df.drop('col1',axis=1))


# Useful methods

# Print the number of columns
print(df.columns)

# Print the type of index
print(df.index)


# Sorting values
print(df.sort_values('col2'))

# Find null values
print(df.isnull())

# Create a new data frame
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)

# Creating a pivot table
print(df.pivot_table(values='D', index=['A','B'],columns=['C']))