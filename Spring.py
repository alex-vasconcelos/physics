
"""
A very simple oscillation of a spring (perfect environment, no energy loss)
Code is written with the Verlet method to preserve energy
@author: alex
"""

from numpy import sqrt, pi
from pylab import plot, xlabel, ylabel, show


def accel(x):
    # returns acceleration for a given position, x
    return (-c*x)


c = 1.0
x = 1.0
v = 0
t = 0

# lists for the position, time, and velocity
xpoints = [x]
tpoints = [t]
vpoints = [v]
pipoints = [t]

# sets the time step based off the number of periods and the number of steps
# we initialize
periods = 3
t_fin = periods*2*pi*sqrt(1/c)
Nsteps = periods*20
h = t_fin/Nsteps

print(t,"\t\t\t",x,"\t\t\t",v)

# loops through the number of steps and updates acceleration, position, velocity, time
# using the verlet algorithm, prints these values for each loop
for i in range(Nsteps):
    a = accel(x)
    v += .5*h*a
    x += h*v
    xpoints.append(x)
    a = accel(x)
    v += .5*h*a
    vpoints.append(v)
    t += h
    tpoints.append(t)
    pipoints.append(t/pi)
    print(t,"\t",x,"\t",v)

# graphs with respect to seconds
plot(tpoints, xpoints)
xlabel("t")
ylabel("x(t)")
show()

# graphs with respect to pi seconds
plot(pipoints, xpoints)
xlabel("t in pi seconds")
ylabel("x(t)")
show()


