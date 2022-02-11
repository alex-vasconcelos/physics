#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brownian Motion/Random Walk
Returns a graph of the probability function for different distributions
"""

from numpy import random, sum, multiply
from numpy import mean, std, histogram, empty, arange
import matplotlib.pyplot as plt
from scipy.stats import norm


s = 0.5

tsteps = 200
Nparticle = 500_000

xlist = empty(Nparticle)


# returns random displacement of particle in a given time step
#def jump():
#    if random.random() < 0.5:
 #       return s
  #  else: 
   #     return -s
    

for p in range(Nparticle):
    """
    x = 0
    
    for t in range(tsteps):
        x += jump()
        
    xlist[p] = x
    """
    
    # move +/-s per time step
    path = (random.randint(low=-1,high=1,size=tsteps) + 0.5) * 2
    
    # move pdf: uniform on [-1,1]
    #path = random.uniform(low=-1,high=1,size=tsteps)
    
    # move pdf: symmetric triangular on [-1,1]
    #path = random.triangular(left=-1,mode=0,right=1,size=tsteps)
    
    # move pdf: symmetric triangular on [-1,1]
    #path = random.normal(loc=0,scale=1,size=tsteps)
    
    # move pdf: normal distribution
    #path = random.normal(loc=0,scale=1,size=tsteps)
    
    #move pdf: Poisson distribution, random sign
    #signs = (random.randint(low=-1,high=1,size=tsteps) + 0.5) * 2
    #draws = random.poisson(lam=1,size=tsteps)
    #path = draws * signs
    
    xlist[p] = sum(path) * s
    
    
# evaluate some statistical measures and plot pdf
mean_x = mean(xlist)
sigma = std(xlist)
print("mean = ", mean_x, "\t sigma^2/n = ", sigma**2/tsteps)

# rescale final x by sigma
xlist /= sigma

#(counts, bins) = histogram(xlist, bins=30, density=True)
#plt.hist(bins[:-1], bins, weights=counts/Nparticles)

# probabilty density function p(x) at the final time
plt.hist(xlist, bins=30, density=True, histtype='stepfilled')


plt.grid(True)
plt.xlabel("x / " + r"$\sigma$")
plt.ylabel("p(x/" + r"$\sigma$)")


# superimpose Gauss normal distribution
x_axis = arange(-4, 4, 0.01)
plt.plot(x_axis, norm.pdf(x_axis, 0., 1.))
    