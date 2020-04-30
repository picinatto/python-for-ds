import numpy as np
import pandas as pd

''' 

    DATA FRAMES 

'''
print('\n*************\nGroup by in Pandas\n*************\n')


# Create the data
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
# Create the dataframe
df = pd.DataFrame(data)
print(df)

# Create the grouped by company object
grouped_company = df.groupby('Company')

# Get the mean for each company
print(grouped_company.mean())

# Get the sum for each company
print(grouped_company.sum())

# Get the sum agg and select one company
print(grouped_company.sum().loc['FB'])

# Can write everything in the same line
print(df.groupby('Company').sum().loc['FB'])

# Group by with describe
print(df.groupby('Company').describe())

# Can transpose
print(df.groupby('Company').describe().transpose())