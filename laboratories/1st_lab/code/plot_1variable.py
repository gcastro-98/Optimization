# Plot x^2

# This is for python notebook. Uncomment if you are using notebook
matplotlib inline

# This is for Linux KDE. Comment if you are not using it.
import matplotlib
#matplotlib.use('Qt5Agg')

# This is general
import matplotlib.pyplot as plt
import numpy as np

# _Function to plot
X = np.arange(-5, 5, 0.25)
Y = X**2; 

# Plot 
line, = plt.plot(X, Y)
plt.show()

