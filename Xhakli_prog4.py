# Lab 4: Physics
# @author Taulant Xhakli
# @version 1.0
import numpy as np
import math


def find_time(z,h_0):
    g = 9.8 # acceleration of gravity
    t = np.sqrt(2*(h_0 - z)/g)
    return t

y = np.arange(10,0,-0.5)
h_0 = 10
t = find_time(y,h_0)
print('y\narray({})\n'.format(y))
print('t\narray({})\n'.format(t))

# calculating the delta for y, and t.
# divide the two to get the v(velocity).
d_y = y[1:] - y[:-1]
d_t =t[1:] - t[:-1]
v = d_y/d_t
print('v\narray({})\n'.format(v))
