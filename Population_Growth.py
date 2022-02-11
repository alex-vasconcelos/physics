# -*- coding: utf-8 -*-
"""
Monte Carlo simulation for population growth, 
including non-linear "saturation" effect
This is with t = 4 / growth_rate
Alex Vasconcelos
"""

from numpy import exp, sqrt, mean, std
import matplotlib.pyplot as plt
from random import random

growth_rate = .5

N0 = 2

Nmax = 10000

# time step h needs to be h*growth_rate << 1
h = .01 / growth_rate  

runs = 4000
Nlist = []

for r in range(runs):
    print(r)
    N = N0
    t = 0
    
    while t < 4/growth_rate:
        newN = N
        for i in range(N):
            # decide whether we add one or take one from the population
            prob = growth_rate*h # probability we add one
            if random() < prob:
                newN += 1
                
            prob = growth_rate*h * N/Nmax # probability we subtract one
            if random() < prob:
                newN -= 1
                
        t += h
        N = newN
    Nlist.append(N)
    
    
# This is the exact analytical average evolution
avgN = N0*exp(4)/(1+N0/Nmax * (exp(4)-1))
print("average evol: N(t*growth_rate=4) =  ", avgN)

#plt.xscale('log')
#plt.yscale('log')

s = std(Nlist)
print("<N> = ", mean(Nlist), " +/-", s/sqrt(runs))
print("std. dev. sigma = ", s)

plt.grid(True)
plt.xlabel("N")
plt.ylabel("p(N)")
plt.hist(Nlist, bins=25, histtype='stepfilled')
plt.show()

