# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to convert kelvin to fahrenheit when a user inputs a temperture in kelvin
#
###############################
# CITATIONS
#
# https://www.vedantu.com/maths/conversion-of-temperature 
# Access Date: 9/5/2023
#
#  F = (K – 273.15) × 9 ⁄ 5 + 32        k = kelvin f = fahrenheit 

k = float(input("Pick a number that represents degrees Kelvin: "))

def kelvinToFahrenheit(k):
    f = (k - 273.15)*9/5+32
    return f
f = kelvinToFahrenheit(k)
f = str(f)
k = str(k)

print("The temperature converted from " + k + " Kelvin to Fahrenheit is " + f + " degrees Fahrenheit.")