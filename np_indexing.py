import numpy as np
print('\n*************\nIntro to Numpy Arrays\n*************\n')
# Generate the sample array
arr = np.arange(0,11)

print(f'The sample array is: {arr}')

# Using [] to get only one number by its index position
print(arr[3])

# Using slice to select several numbers
print(arr[1:5])

# To get everything up to index 5 | Also works to get the 5th until the end [5:]
print(arr[:6])

# Numpy arrays differ from normal arrays because they can broadcast
# The 100 will broadcast (override) the first 4 elements of the array
arr[0:5] = 100
print(arr)

# To broadcast the whole array use [:]
arr[:] = 0

# Notice that the slice is just a view of the array, it does not copy
# If you want to copy, need to specify
copy_arr = arr.copy()
print(copy_arr)

# Create an 2d array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

# Two methods to get single elements from a 2d array
# [r][c]
print(arr_2d[1][0])
# Use commas
print(arr_2d[1,0])

# To get the elements for right corner [10 -> 30]
#[:2] => Get all rows until the second
#[1:] => Get the second until the end column 
print(arr_2d[:2,1:])


# Using conditions in NP Arrays
print('\n*************\nConditional Arrays\n*************\n')
arr = np.arange(0,11)
print(arr)

# Test a condition in an array
bool_array = arr > 5
print(bool_array)
# To get only the truthy values
print(arr[bool_array])

# More commonly we would see in one line
print(arr[arr>5])

# Create a 5 to 10 array
arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
