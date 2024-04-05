# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to calculate the volume of a sphere using input from a user for the radius
#
###############################
# CITATIONS
#
# https://byjus.com/maths/volume-of-sphere/
# Access Date: 9/5/2023
#
# v =  4/3πr**3   v = volume  where as r = radius
import math
r = float(input("Pick a number any number: "))
def sphereVolume(r):
    v = 4/3*math.pi*r**3
    return v
v = sphereVolume(r)
r = str(r)
v = str(v)

print("The volume of a sphere with a radius of " + r + " is " + v + ".")
