# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:57:52 2019
@author: INISA
"""

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import cos
from math import sin





fig = plt.figure()
ax = fig.gca(projection='3d')


r = 15
v = 0.08
t = [i+1 for i in range(600)]
theta = [(v*t[i])/r for i in range(600)]
x = [r*cos(theta[i]) for i in range(600)]
y = [r*sin(theta[i]) for i in range(600)]
z = [0 for i in range (600)]




t = input("temps (en secondes) = ")

print("x =",x[int(t)],"m")
print("y =",y[int(t)],"m")
print("theta =",theta[int(t)],"rad")
print("Distance parcourue =",theta[int(t)]*r,"m")


ax.plot(x,z,y, label ='Trajectoire Drone', color ="red" , linewidth=2.0, linestyle="-")

ax.scatter(x[int(t)], z[int(t)],y[int(t)],marker='o',color='blue')
 
ax.plot(x[:int(t)], z[:int(t)], y[:int(t)],label ='Distance parcourue par le cubesat', color='blue')

ax.legend()
plt.show()














    

    









