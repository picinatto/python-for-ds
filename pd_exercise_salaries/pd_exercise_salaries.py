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

# What is the name of highest paid person including benefits
print(sal.loc[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName'])

# What is the name of the lowes payed person including benefits
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName'])

# What is the mean Base pay for all employees per year
print(sal.groupby('Year')['BasePay'].mean())

# How many unique job title are there
print(sal['JobTitle'].nunique())

# What are the top 5 most common jobs
print(sal['JobTitle'].value_counts().head())