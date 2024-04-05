# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to convert celsius to kelvin when a user inputs a temperture in celsius
#
###############################
# CITATIONS
#
# https://byjus.com/chemistry/celsius-to-kelvin/ 
# Access Date: 9/5/2023
#
#  k = c + 273.15  c = celsius k = kelvin 

c = float(input("Pick a number that represents degrees celcius: "))

def celsiusToKelvin(c):
    k = c + 273.15
    return k
k = celsiusToKelvin(c) 
c = str(c)
k = str(k)

print("The temperature converted from " + c + " degrees Celsius to Kelvin is " + k + " Kelvin.")