import pandas as pd

# Reading the data file from csv
sal = pd.read_csv('pd_exercise_salaries/Salaries.csv')

print(type(sal))

# Print the first 5 rows
print(sal.head())

# Print info for the file
print(sal.info())

# Get the average base pay
print(sal['BasePay'].mean())

# Get the highest amount of OvertimePay
print(sal['OvertimePay'].max())

# Job title for JOSEPH DRISCOLL
print(sal.loc[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])

# How much JOSEPH DRISCOLL makes including benefits
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])