import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)

print(df)

# Drop NA rows
print(df.dropna())

# Drop NA columns
print(df.dropna(axis=1))

# Only drop rows that more NA values than the threshold
print(df.dropna(thresh=2))

## 
## Fill NA
##
print(df.fillna(value='Fill Value'))

# Fill with column calculated values
print(df['A'].fillna(value=df['A'].mean()))