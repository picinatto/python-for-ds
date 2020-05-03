import numpy as np
import matplotlib.pyplot as plt

# Creating the data
x = np.linspace(0,5,11)
y = x ** 2

##
## CUSTOMIZING THE PLOT
##

# CUSTOMIZING COLOR, LINEWIDTH AND ALPHA
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
# Setting the color and line width and alpha (transparency)
ax.plot(x,y,color='#FF8C00',lw=3,alpha=0.5)
#plt.show()

# CUSTOMIZING THE LINESTYLE
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
# Customizing the line style
ax.plot(x,y,linestyle='--') # Or ls
#plt.show()

# ADDING MARKERS
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,marker='o',markersize=20)
plt.show()