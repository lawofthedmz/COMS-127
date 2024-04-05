#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
#  Murphy Glawe             9/25/2023
# 
#           [COMS 127 Section 6]
#  LabWeek 6 
# Citations::: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing  Accessed 9/25/2023
#
#
# Description: Using the lsystem type code and modifying to make turtle draw random instances of tridecagons 


import turtle 
import random
def pcmd(t):
    x = random.randint(-200, 200)  # Adjust the range as needed
    y = random.randint(-200, 200)  # Adjust the range as needed
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    
def tridecagonTurtle(t):
    for i in range(13):
        t.forward(10)
        t.left(27 + (9/13))
def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'TP-+TP+TP-P+FTP+-TP'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
            
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'T':
            tridecagonTurtle(aTurtle)
        elif cmd == 'P':
            pcmd(aTurtle)
        
       

    

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(100)
    drawLsystem(t, inst, 60, 35)   # draw the picture
                                  # angle 60, segment length 5
    
    wn.exitonclick()

main()