import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time
import collections

class Point(object):
    # creates point given x, y coords
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    
def midpoint(u, v):
    return Point((u.x + v.x)/2.0, (u.y + v.y)/2.0)

def transform(p, iter):
    for j in range(iter):
        p = helper(p)
    return p

def helper(p):
    newP = []
    for i in range(-1, len(p) - 1, 1):
        u, v = p[i], p[i + 1]
        newP.append(midpoint(u, v))
    return newP

# generate n points on perimeter of a unit circle
def circularPoints(n):
    return [Point(math.cos((2 * i * math.pi)/n), math.sin((2 * i * math.pi)/n)) for i in range(n)]


# print(points)
points = circularPoints(10)
coord = [(v.x, v.y) for v in points]
coord.append(coord[0]) #repeat the first point to create a 'closed loop'
x, y = zip(*coord) #create lists of x and y values

plt.figure()
plt.plot(x,y) 
plt.show() 