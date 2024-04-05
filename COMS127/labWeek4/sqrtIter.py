# Murphy Glawe          9.13.2023
#
# Lab Week 4 Section 6
#
# Description: Taking input from a user for x = an integer and iterations = number of time to run for loop //// the equation while find 
# the square root of x using the approximation method. the higher the iterations the closer the answer is to the real sqrt
#
# Citations:   https://www.cuemath.com/algebra/square-root-of-2/ accessed 9/13/2023
 
print("Murphy Glawe         [COM S 127 J]")
print()
print("(9/13/2023)")
print()
def sqrtIter(x, iterations): 
    
    if x <= 0:
        print("ERROR! ERROR! ERROR! Please input postive integer.")
    else:
        y = (x + 1)/2
        for i in range(iterations):
            y = ((x / y) + y)/2
        return y 


x = int(input("Pick the value 'x' you want to take the square root of: "))
iterations = int(input("Pick the number of time you want to iterate: "))


print(sqrtIter(x, iterations))

