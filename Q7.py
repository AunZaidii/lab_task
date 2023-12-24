# Q7: A Stone is dropped freely from a height of 100 feet. With what velocity will it hit the ground?
# (Neglect the air resistance and assume the acceleration due to gravity is 32ft/s2).
import math as maths
s = 100
g = 32
u = 0
# v = ?
v = maths.sqrt((2*g*s)+(u**2))
print("The stone will hit the ground with the velocity of",v,"ft/s")