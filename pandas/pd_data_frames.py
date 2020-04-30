import numpy as np
import pandas as pd
from numpy.random import randn

''' 

    DATA FRAMES 

'''
print('\n*************\nData Frames in Pandas\n*************\n')

# Adjusting the random method to get the same results from the lecture
np.random.seed(101)

# Creating a 
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)