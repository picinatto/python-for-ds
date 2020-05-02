import numpy as np
import matplotlib.pyplot as plt

# Creating the data
x = np.linspace(0,5,11)
y = x ** 2

## Functions method

# Create the figure with functions
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
#plt.show()

# Multiplots in the same canvas
plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')
#plt.show()


## Using the Object Oriented Method
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set title')
#plt.show()


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.5,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes2.plot(y,x)
plt.show()