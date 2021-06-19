
# Using Archimedes' method to find an approximation of pi
# author: Taulant Xhakli
# version: 1.0
import math

numSides = 8

innerAngleB = 360.0 / numSides
halfAngleA = innerAngleB / 2

oneHalfSides = math.sin(math.radians(halfAngleA))
sides = oneHalfSides * 2

polygonCircumference = numSides * sides

pi = polygonCircumference / 2
# enter pi in the python shell to
# output rough estimate.
