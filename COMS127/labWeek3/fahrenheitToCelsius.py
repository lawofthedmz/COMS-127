# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to convert fahrenheit to celsius when a user inputs a temperture in fahrenheit
#
###############################
# CITATIONS
#
# https://www.uptodate.com/contents/calculator-temperature-unit-conversions#:~:text=Temperature%20in%20degrees%20Celsius%20(°C)%20%3D%20(Temperature%20in,-%2032)%20*%205%2F9
# Access Date: 9/5/2023
#
#   c = (f - 32) * 5/9 c = celsius f = fahrenheit 

f = float(input("Pick a number that represents degrees Fahrenheit: "))

def fahrenheitToCelsius(f):
    c = (f -32)*5/9 
    return c
c = fahrenheitToCelsius(f)
f = str(f)
c = str(c)

print("The temperature converted from " + f + " degrees Fahrenheit to Celsius is " + c + " degrees Celsius.")