from __future__ import division
from numpy import arange
from pylab import meshgrid, cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import math

import random
import numpy as np

def lin_func(x):
    return 2*x - 10 + 3*random.gauss(10, 2)

x = arange(0, 10, 0.1)
y = np.array([lin_func(i) for i in x])

#x = [-2, -1, 1, 4]
#y = [-3, -1, 2, 3]

y2_mean = sum(np.array([num*num for num in y]))/len(y)
x_y_mean = sum(np.array([i*j for i, j in zip(x, y)]))/len(y)
y_mean = sum(np.array([num for num in y]))/len(y)
x2_mean = sum(np.array([num*num for num in x]))/len(x)
x_mean = sum(np.array([num for num in x]))/len(x)
n = len(x)

m_solution = ((x_mean*y_mean - x_y_mean)/(x_mean**2 - x2_mean))
b_solution = y_mean - m_solution*x_mean

def line_fit(x):
    return m_solution*x + b_solution

y_sol = np.array([line_fit(i) for i in x])
plt.plot(x, y, 'ro')
plt.plot(x, y_sol)
plt.show()


# the function that I'm going to plot
def SE_func(m,b):
    return (n*y2_mean - 2*m*n*x_y_mean - 2*b*n*y_mean + (m**2)*n*x2_mean + 2*m*b*n*x_mean + n*b**2)
    
 
x = arange(-10.0, 10.0, 0.1)
y = arange(-10.0, 10, 0.1)
X,Y = meshgrid(x, y) # grid of point
Z = SE_func(X, Y) # evaluation of the function on the grid

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.plot((m_solution, b_solution), 'ro')
plt.show()

print SE_func(m_solution, b_solution)


from math import cos, sin, pi

def x(t):
    return 5*t + 10

def y(t):
    return 50 - (10*t**2)/2
    
t_array = arange(0, 3.0, 0.01)

X = [x(t) for t in t_array]
Y = [y(t) for t in t_array]

plt.plot(X, Y)