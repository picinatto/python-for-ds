import numpy as np
import matplotlib.pyplot as plt

# Creating the data
x = np.linspace(0,5,11)
y = x ** 2

## 
## FUNCTIONS METHOS
##

# Create the figure with functions
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
#plt.show()

# MULTIPLOTS
# Multiplots in the same canvas
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
#plt.show()

##
## OBJECT ORIENTED METHOD
##

## CREATING FIGURES WITH OO METHOD
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set title')
#plt.show()

# SUBPLOTS MANUALLY
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.5,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x)
#plt.show()


# SUBPLOTS SHORT SINTAX
# Short sintax for starting the subplots
# The axes in this case is created automatically a list of axes
fig,axes = plt.subplots(nrows=1,ncols=2)
# Can plot both with the same data: axes.plot(x,y)
# Or plot with diferente data:
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')
#plt.show()


##
## FIGURE SIZE AND DPI
##

# SET THE FIGURE SIZE
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
#plt.show()

# SAVE THE FIGURE (PDF, PNG, JPEG)
#fig.savefig('my_picture.png')

# ADDING LEGENDS
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label='X Squared')
ax.plot(x,x**3, label='X Cubed')
# Can set the location
ax.legend(loc=(0.1,0.8))
plt.show()