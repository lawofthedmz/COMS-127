# Murphy Glawe              9/14/2023
#
#   Lab Week 4 Section 6 
#
# Description: Taking input from user for sidelengths and x & y coordinates make a tridecagon 
#
# Citations: https://www.google.com/search?client=opera-gx&q=tridecagon+angles&sourceid=opera&ie=UTF-8&oe=UTF-8 
#
# 27 and 9/13 per angle 13 time

sinput = int(input("Choose a the sidelengths of the Tridecagon: "))
xinput = int(input("Choose an x cordinate: "))
yinput = int(input("Choose a y coordiante: "))
colorinput = input("What color do you want your tridecagon to b?: ")
import turtle
tri = turtle.Turtle()

tri.pencolor(colorinput)
tri.pensize(10)
def tridecagonTurtle(s, x, y):
    
    tri.penup()
    tri.setposition(x, y)
    tri.pendown()
    
    for i in range(13):
        tri.forward(s)
        tri.left(27 + (9/13))

tridecagonTurtle(sinput, xinput, yinput)

wn = turtle.exitonclick()