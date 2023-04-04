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

# example 1 --->
# coords = [[59.9368965035457, 98.34598093434701], [18.971402528372284, 69.22670356770257], [51.71330148707602, 81.61041412085348], [285.9817248144231, 146.13546614317997], [220.03663830181705, 170.8542693987106], [155.86824608973367, 200.85108245340956], [114.68093250819196, 294.04609056392013], [9.916543477674278, 231.15932759422427], [126.3664369580382, 160.68014536162062], [49.48329780339944, 156.4198489327802]]
# points = [Point(v[0], v[1]) for v in coords]
# coords.append(coords[0]) #repeat the first point to create a 'closed loop'
# x, y = zip(*coords) #create lists of x and y values


# result = list((v.x, v.y) for v in transform(points, 1))
# result.append(result[0])
# xr, yr = zip(*result)
# plt.figure()
# plt.plot(x, y) 
# plt.plot(xr, yr)
# plt.show() 

# --------------------------------------------------------------------------

# example 2 --->
# coords =  [[61.17176716101951, 146.28833165608333], [20.284787672711246, 78.08349892010564], [126.20661538601328, 125.50725421886064], [228.35689427355248, 61.684109206312954], [269.37108443296853, 57.26101924905451], [246.57350723449912, 135.87863598910127], [219.2090940297828, 158.09041994851967], [158.57160798947024, 211.20029731252112], [121.02347257084534, 282.05003635233413], [119.16672624710303, 209.64963447977954]]
# points = [Point(v[0], v[1]) for v in coords]
# coords.append(coords[0]) #repeat the first point to create a 'closed loop'
# x, y = zip(*coords) #create lists of x and y values


# result = list((v.x, v.y) for v in transform(points, 3))
# result.append(result[0])
# xr, yr = zip(*result)
# plt.figure()
# plt.plot(x, y) 
# plt.plot(xr, yr)
# plt.show() 

# --------------------------------------------------------------------------

# example 3 --->
# coords =  circularPoints(10)
# points = [(v.x, v.y) for v in coords]
# points.append(points[0]) #repeat the first point to create a 'closed loop'
# x, y = zip(*points) #create lists of x and y values


# result = list((v.x, v.y) for v in transform(coords, 5))
# result.append(result[0])
# xr, yr = zip(*result)
# plt.figure()
# plt.plot(x, y) 
# plt.plot(xr, yr)
# plt.show() 