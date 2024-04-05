# Murphy Glawe              9/5/2023
#
# Lab Week 3 Section 6
#
# Goal of this code is to convert celsius to fahrenheit when a user inputs a temperture in celsius
#
###############################
# CITATIONS
#
# https://www.uptodate.com/contents/calculator-temperature-unit-conversions#:~:text=Temperature%20in%20degrees%20Celsius%20(°C)%20%3D%20(Temperature%20in,-%2032)%20*%205%2F9
# Access Date: 9/5/2023
#
#  f= c*9/5+32 c = celsius f = fahrenheit 



def celsiusToFahrenheit(c):
    f = c*9/5+32
    return f



print(f"The temperature converted from {float(input('Pick a number that represents degrees Celsius: '))} degrees Celsius to Fahrenheit is {print(celsiusToFahrenheit(0))}degrees Fahrenheit.")