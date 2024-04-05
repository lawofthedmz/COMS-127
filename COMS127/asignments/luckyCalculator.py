

# Murphy Glawe              9/11/2023
# luckyCalculator/ Asignmnet #2
# A Program that gives you three options, a calculator, a lucky number between range generator and a quit option

import random

# NOTE: Function definitions should go here!
def addition(l, r):
    answer = l + r
    return answer
def subtraction(l, r):
    answer = l - r
    return answer
def multiplication(l, r):
    answer = l * r
    return answer
def division(l, r):
    if r == 0:
        print("ERROR! No division by zero. Changed integer to 1.")
        r = 1
    answer = l / r
    return answer
def floorDivision(l, r):
    if r == 0:
        print("ERROR! No division by zero. Changed integer to 1.")
        r = 1
    anwser = l // r
    return anwser
def divRemainder(l, r):
    if r == 0:
        print("ERROR! No division by zero. Changed integer to 1.")
        r = 1
    answer = l % r
    return answer
def exponential(l, r):
    answer = l ** r
    return answer
def calculator(c, l, r):
    list = ('+', '-', '*', '/', '//', '%', '**')
    if c not in list: 
        answer = print("ERROR ERROR ERROR! Please pick one of these calculations: [+], [-], [*], [/], [//], [%], [**]")
    else:
        if c == '+':
            answer =addition(l, r)
        elif c == '-':
            answer =subtraction(l, r)
        elif c == '*':
            answer =multiplication(l, r)
        elif c == '/':
            answer =division(l, r)
        elif c == '//':
            answer =floorDivision(l, r)
        elif c == '%':
            answer =divRemainder(l, r)
        elif c == '**':
            answer =exponential(l, r)

    return answer    
def lnumberInput(lefn):
        lefn = int(input("Pick you first number: "))
        return lefn
def rnumberInput(rightn):
        rightn = int(input("Pick your second number: " ))
        return rightn 
def luckyNumber(a, b):
    returnValueVariable = 0
    if a < b:
        returnValueVariable = random.randint(a, b+1)
    else:
        returnValueVariable = random.randint(b, a+1)
    return returnValueVariable

print("Lucky Calculator!")
print()


print("By: Murphy R. Glawe")
print("[COM S 127 J]")
print()

# Determine initial player choice
print("What would you like to do?")
print()
choice = input("[c]alculator, [l]ucky number, [q]uit: ")
print()

# initial choice tasks (1 pt.) ----------------------------------------------------------------------------------------------------------------
if choice == 'c':
    print("You chose the calculator, lets calculate!")
    print()
    calcc = str(input("Pick one of these calculations: [+], [-], [*], [/], [//], [%], [**]: "))
    ln = lnumberInput(0)
    rn = rnumberInput(0)
    ans = calculator(calcc, ln, rn)
    print(f"The answer is {ans}")
#----------------------------------------------------------------------------------------------------------------------------------------------
#  a section of code that executes if the user enters 'l' as their initial choice instead of 'c' or 'q'.
elif choice == 'l':
    print("You chose lucky number. Lets get lucky.")
    a = lnumberInput(0)
    b = rnumberInput(0)
    luck = luckyNumber(a, b)
    print(f"Your lucky number is {luck}")
#  a section of code that executes if the user enters 'q' as their initial choice instead of 'c' or 'l'.
elif choice == 'q':
    print("You chose to quit. Get out of here then loser.")
# another section of code where if the user does not enter 'c', 'l', or 'q' in their initial choice, the script will print out an 
#       error message stating: 
else:
    print("Invalid response please choose 'c', 'l', or 'q' ")

# ---------------------------------------------------------------------------------------------------------------------------------------------

