# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to convert fahrenheit to kelvin when a user inputs a temperture in fahrenheit
#
###############################
# CITATIONS
#
# https://www.vedantu.com/maths/conversion-of-temperature 
# Access Date: 9/5/2023
#
#  K = (F − 32) × 5 ⁄ 9 + 273.15 k = kelvin f = fahrenheit 

f = float(input("Pick a number that represents degrees Fahrenheit: "))

def fahrenheitToKelvin(f):
    k = (f -32)*5/9+273.15
    return k
k = fahrenheitToKelvin(f) 
f = str(f)
k = str(k)

print("The temperature converted from " + f + " degrees Fahrenheit to Kelvin is " + k + " Kelvin.")