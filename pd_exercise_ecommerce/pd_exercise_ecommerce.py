import pandas as pd

# Get the data from the csv file
ecom = pd.read_csv('pd_exercise_ecommerce/Ecommerce Purchases')

# Display the firs five record
print(ecom.head())

# Display the columns
print(ecom.info())

# Get the average purchase price
print(ecom['Purchase Price'].mean())

# Get the highest purchase price
print(ecom['Purchase Price'].max())

# Get the lowest purchase price
print(ecom['Purchase Price'].min())

# How many people have English 'en' as their Language of choice on the website?
print(ecom[ecom['Language'] == 'en'].count())

# How many people have the job title of "Lawyer" ?
print(ecom[ecom['Job'] == 'Lawyer'].count())

# How many people made the purchase during the AM/PM?
print(ecom['AM or PM'].value_counts())

#What are the 5 most common Job Titles?
print(ecom['Job'].value_counts().head())

# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? 
print(ecom.loc[ecom['Lot'] == '90 WT']['Purchase Price'])

#What is the email of the person with the following Credit Card Number: 4926535242672853
print(ecom.loc[ecom['Credit Card'] == 4926535242672853]['Email'])

# How many people have American Express as their Credit Card Provider *and made a purchase above $95
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

# How many people have a credit card that expires in 2025?
ecom['ExpirationYear'] = ecom['CC Exp Date'].str[3:5]
print(ecom[ecom['ExpirationYear'] == '25'].count())

# What are the top 5 most popular email providers/hosts
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))