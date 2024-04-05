# Murphy R. Glawe           9/11/2023
#
# LabWeek 4 
#
#
# Goal of this Asignmnet: 
#  a function that takes the three integers as input, it will calculate the sum of c random numbers
# in a range between a through b + 1
#
#

import random 

print("Murphy Glawe     [COM S 127 J]")
print()
print("9/11/2023")
print()
def randomSum(a, b, c):

    sum = 0
    for i in range(c):
        randomNumber = random.randint(a, b - 1)
        sum += randomNumber
    return sum 
# Getting Input for a, b, and c
a = int(input("Please pick a number for a: "))
b = int(input("Please pick a number for b: "))
c = int(input("Please pick a number for c: "))

# final_result function that puts together the input from a, b, and c 
final_result = randomSum(a, b + 1, c)

a_s = str(a)
bs = str(b)
cs = str(c)
final_result_s = str(final_result)

print("The sum of " + cs + " random numbers between " + a_s + " and "  + bs + " is " + final_result_s + ".")


        

