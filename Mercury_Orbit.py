#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orbit of Mercury
Uses Verlet method to conserve energy and angular momentum
@author: alex
"""
from numpy import sqrt, array, arange, dot, cross
import matplotlib.pyplot as plt

mSun = 1.9891e30
G = 6.6738e-11
mMercury = .33011e24
def accelGravity(R):  
    # returns acceleration based off position
    r = sqrt(dot(R,R))
    ax = -G*mSun/r**3 * R[0]
    ay = -G*mSun/r**3 * R[1]
    
    return array([ax,ay],float)

def Energy(R,V):
    # returns energy based off position and velocity
    r = sqrt(dot(R,R))
    Epotential = -G*mSun*mMercury/r
    Ekinetic = 0.5*dot(V,V)*mMercury
    return Epotential + Ekinetic



OneYear = 88 * 24 * 60 * 60  #This is one year in seconds
N = 360  #This is the number of steps
h = OneYear/N  #This is the time step


tpoints = arange(0.0,OneYear,h)

xpoints = []
ypoints = []
vxpoints = []
vypoints = []
energylist = []
angularmomentumlist = []

r = array([46.002e9,0])
v = array([0,58.98e3])

xpoints.append(r[0])
ypoints.append(r[1])


Einitial = Energy(r,v)
Lz_initial = cross(r,v) # Lz is angular momentum

# runs 100 orbits, but only graphs every tenth orbit
for orbits in range(100):
    for t in tpoints:
        v += h/2 * accelGravity(r)  #update the velocity half step
        r += v*h  #update the position
        v += h/2 * accelGravity(r)  #update the velocity another half step
        
        E = Energy(r,v)/Einitial
        
        Lz =cross(r,v)
        
        if orbits % 10 == 0:
            print(E, Lz/Lz_initial)
            energylist.append(Energy(r,v))
            xpoints.append(r[0])
            ypoints.append(r[1])
            angularmomentumlist.append(cross(r,v))

print("Einitial: ",Einitial)
print("Eending: ",energylist[int(len(energylist)/2)])
print("plotting ",len(xpoints), " points")
print(xpoints[0], ypoints[0])
print(xpoints[len(xpoints)-1], ypoints[len(ypoints)-1])
plt.plot(xpoints, ypoints)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('square')
plt.show()        

plt.plot(tpoints, energylist)
plt.xlabel("time")
plt.ylabel("energy")
plt.ylim(-9e32,0)
plt.show()

plt.plot(tpoints, angularmomentumlist)
plt.xlabel("time")
plt.ylabel("momentum")
plt.ylim(angularmomentumlist[0]-200,angularmomentumlist[0]+200)
plt.show()





