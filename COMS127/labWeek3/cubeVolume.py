# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to calculate the volume of a cube using input from a user for the length
#
###############################
# CITATIONS
#
# https://tutors.com/lesson/volume-of-a-cube
# Written by Malcom Mckinsey and Published January 28, 2023. Access Date: 9/5/2023
#
# v = s**3    v = volume  where as s = side length

s = float(input("Pick a number any number: "))
def cubeVolume(s):
    v = s**3
    return v
v = cubeVolume(s)
s = str(s)
v = str(v)

print("The volume of a cube with the side lengths of " + s + " is " + v + ".")
