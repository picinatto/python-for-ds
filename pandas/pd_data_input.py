import numpy as np
import pandas as pd

# Reading CSV File
df_csv = pd.read_csv('example.csv')
print(df_csv)

# Write to a csv file
df_csv.to_csv('my_output.csv',index=False)

# Read from excel file
df_excel = pd.read_excel('Excel_Sample.xlsx')
print(df_excel)

# Write to an excel file
df_excel.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

# Reading from html
df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df_html)

# Reading from SQL
from sqlalchemy import create_engine
# Create in memory SQL lite database
engine = create_engine('sqlite:///:memory:')
# Write data to this SQL table
df_csv.to_sql('my_table',engine)
# Get the information from the SQL Table
df_sql = pd.read_sql_table('my_table',con=engine)
print(df_sql)