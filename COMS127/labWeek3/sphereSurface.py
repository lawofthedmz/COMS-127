# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to calculate the surface area of a sphere using input from a user for the radius
#
###############################
# CITATIONS
#
# https://byjus.com/maths/surface-area-of-a-sphere/ 
# Access Date: 9/5/2023
#
# a = 4πr**2 a = surface area where as r = radius 
import math
r = float(input("Pick a number any number: "))

def sphereSurface(r):
    a = 4*math.pi*r**2
    return a
a = sphereSurface(r)
r = str(r)
a = str(a)

print("The surface area of a sphere with a radius of " + r + " is " + a + ".")