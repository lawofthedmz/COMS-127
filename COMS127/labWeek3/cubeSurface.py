# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to calculate the sureface area of a cube using input from a user for the length of a side 
#
###############################
# CITATIONS
#
# https://byjus.com/maths/surface-area-of-cube/#
# Access Date: 9/5/2023
# a = s**3    a = surface area  where as s = side length

s = float(input("Pick a number any number: "))
def cubeSurface(s):
    a = 6*s**2
    return a
a = cubeSurface(s)
s = str(s)
a = str(a)

print("The surafce area of a cube with the side lengths of " + s + " is " + a + ".")