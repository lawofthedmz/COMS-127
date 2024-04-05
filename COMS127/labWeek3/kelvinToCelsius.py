# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to convert kelvin to celsius when a user inputs a temperture in kelvin
#
###############################
# CITATIONS
#
# https://byjus.com/chemistry/celsius-to-kelvin/ 
# Access Date: 9/5/2023
#
#  c = k - 273.15  c = celsius k = kelvin 

k = float(input("Pick a number that represents degrees celcius: "))
def kelvinToCelsius(k):
    c = k - 273.15
    return c
c = kelvinToCelsius(k)
c = str(c)
k = str(k)

print("The temperature converted from " + k + " Kelvin to Celsius is " + c + " degrees Celsius.")