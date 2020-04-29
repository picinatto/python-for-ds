import numpy as np

# Create a numpy array
array_np = np.array([1, 2, 3])
print(f'The one dimension array is: {array_np}')

# Builds a 2 dimensional matrix
array_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nparray = np.array(array_matrix)
print(f'The array matrix is: \n{nparray}')

# Print a range array
range = np.arange(0,10,2)
print(f'The range is: {range}')

# To generate a zeros array use np.zeros
zero_array = np.zeros((2,3))
print(f'Represents the numpy generated zeros array: \n{zero_array}')

# To generate an array of evenly spaced numbers
linspace = np.linspace(0,10,30)
print(f'The evenly spaced numbers array: \n{linspace}')

# Generate identy matrix (# of rows == # of coluns)
i_matrix = np.eye(4)
print(f'The identity matrix is: \n{i_matrix}')

# Generate random numbers
random = np.random.rand(5)
print(f'The list of random numbers between 0 and 1: {random}')

# Generate random numbers for integers low and high
rand_int = np.random.randint(1,100,10)
print(f'The list of 10 random intengers btwn 1 and 100: {rand_int}')

# Discover the index of the max number of the array
max_int = rand_int.argmax()
print(f'The index of the max int in the array is: {max_int}')

# To get the data type inside the array
data_type = rand_int.dtype
print(f'The datatype of the array is {data_type}')