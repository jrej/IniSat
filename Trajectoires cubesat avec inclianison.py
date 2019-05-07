# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:17:43 2019

@author: INISAT
"""


import matplotlib.pyplot as plt
from math import cos
from math import sin
from math import pi





fig = plt.figure()
ax = fig.gca(projection='3d')


r = 15
v = 0.08



t = [i+1 for i in range(600)]
#theta = [(v*t[i])/r for i in range(600)]
theta = [0.1 for i in range(600)]
phi = (30*pi)/180

x = [r*cos(theta[i])*sin(phi) for i in range(600)]
y = [r*sin(theta[i])*sin(phi) for i in range(600)]
z = [r*cos(phi) for i in range (600)]

t = input("temps (en secondes) = ")

print("x =",x[int(t)],"m")
print("y =",y[int(t)],"m")
print("z =",z[int(t)],"m")
print("theta =",theta[int(t)],"rad")
print("Distance parcourue =",theta[int(t)]*r,"m")


ax.plot(x,z,y, label ='Trajectoire Drone', color ="red" , linewidth=2.0, linestyle="-")

ax.scatter(x[int(t)], z[int(t)],y[int(t)],marker='o',color='blue')
 
ax.plot(x[:int(t)], z[:int(t)], y[:int(t)],label ='Distance parcouruepar le cubesat', color='blue')

ax.legend()
plt.show()







