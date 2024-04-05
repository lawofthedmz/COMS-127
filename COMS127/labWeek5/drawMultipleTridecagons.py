# Murphy Glawe              9/20/2023
#
#   Lab Week 5 Section 6 
#
# Description: Taking input from user for sidelengths and x & y coordinates make  multiple tridecagons  
#
# Citations: https://www.google.com/search?client=opera-gx&q=tridecagon+angles&sourceid=opera&ie=UTF-8&oe=UTF-8 
#
# 27 and 9/13 per angle 13 time
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ")
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⢀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⣀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⣠⠄⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⡜⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⡘⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣿⠛⠛⡿⠛⡿⠛⢿⠿⡿⢿⣿⣿⣶⡈⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡛⢻⣀⣨⣧⣤⣼⣤⣴⡇⠰⢇⣀⣟⣀⣇⣸⣀⡏⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡿⣏⠹⣆⡿⠾⠟⠚⠉⠉⠀⠀⠈⠉⠐⠐⠒⠒⠛⠋⠉⠛⢷⣼⣸⣇⠀⠀⠀⡀⡀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣟⠳⣤⣸⡷⠋⠀⡤⠔⠒⠚⠛⠛⠓⠀⠀⠀⠀⠀⠔⠒⠒⠲⢄⡀⠙⣿⣿⠀⠀⠀⢇⠁⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡳⣬⣷⠟⠁⠀⠀⠀⠀⠄⠒⠒⠀⠀⠈⠷⠀⠀⠀⠀⢸⠀⠀⠤⣄⣀⠀⢿⡇⠀⠀⣰⢾⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⣿⣿⠷⣌⠛⡿⠃⣀⠀⠀⠀⣶⠄⣴⡲⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⣠⣤⣀⣀⡈⠁⣾⠄⠀⠀⡾⡜⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⢻⡻⣦⡉⡿⠃⠀⢸⣷⠆⠀⠀⠀⣘⣻⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⣟⣾⣿⣿⠘⠯⣿⡀⠀⠀⣻⣧⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠰⠈⢷⡈⢻⡇⠀⠀⢸⣿⣿⠆⠀⠀⠈⠉⠙⠟⠛⠁⠀⠀⠀⠀⠸⡇⠈⠹⠟⠓⠂⠀⢼⡇⠀⠀⢇⣆⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠱⠈⠻⣾⡇⠀⠀⢸⣿⣗⡿⣶⡄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠠⠄⣜⣐⣿⡧⠀⣠⡿⠈⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠈⢿⣟⣿⣿⣿⣧⠌⠀⠀⠀⢾⠛⠀⠀⠀⠀⠀⣰⠃⠀⡔⢮⣟⣿⠡⣺⣁⠅⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⣟⣾⣿⣿⣿⣇⡆⣠⠟⣈⣟⣧⠍⣁⡜⡓⠃⡆⢠⣾⣿⡿⠁⢐⣷⠋⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⢘⣾⡾⣿⣾⣽⣿⣛⠴⠋⢜⣟⣋⡑⠙⠋⠛⠿⡶⣵⢸⣿⡿⠁⠀⠈⢸⣆⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⡏⠀⠀⠐⢺⡧⢭⢽⣿⣾⣿⣷⣄⡬⡀⠉⡹⠿⠿⠿⠿⠯⣿⢿⣿⠃⠀⠀⡠⣳⡟⠀⠀⠀⠀⠀")
print(" ⢀⠊⣠⣴⣾⣿⣿⣿⣿⣿⠁⠀⠀⠀⢨⣠⢟⢮⣿⣫⢿⣿⣿⣿⣿⣿⣿⣶⣾⣶⣶⣴⣿⡿⠿⣢⡄⠛⠊⠁⠀⠀⠀⠀⠀⠀")
print(" ⠀⢴⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⢀⣨⠝⡃⡟⠾⡪⣑⢻⢿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣷⣄⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⢸⣿⣿⣿⣿⣿⣿⣯⣤⣤⣄⣰⠋⠀⠀⠀⠈⠁⠛⠾⡛⠧⡖⣿⣛⣻⠜⣿⣿⣿⣿⣿⣿⣿⣷⣤⡈⠂⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠃⠋⠆⠓⠉⠃⠊⣡⣭⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣄⣀⠀⠀⠀")
print(" ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢶⣾⡷⠦⣤⡤⣶⣶⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦")
print(" ⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠒⠛⠛⠛⠛⠛⠓⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛ ")     
                                                                                                     

                                                                                                     

def main():
    # input functions
    slinput = int(input("Choose a the sidelengths of the Tridecagon(s): "))
    xinput = int(input("Choose an x cordinate: "))
    yinput = int(input("Choose a y coordiante: "))
    numi = int(input('How many TriDecagons do you want to draw?: '))
    space = int(input('Dude, how much space do you want in between each tridecagon?: '))
    # import turtle
    import turtle
    tri = turtle.Turtle()
    tri.pensize(5)

    def drawMultipleTridecagons(s, x, y, ni, sp):
     
        for i in range(ni):
            tridecagonTurtle(s, x, y)
            x += sp 
    def tridecagonTurtle(s, x, y):
    
        tri.penup()
        tri.setposition(x, y)
        tri.pendown()
    
        for i in range(13):
            tri.forward(s)
            tri.left(27 + (9/13))
    
    # call multiple tridec function
    drawMultipleTridecagons(slinput, xinput, yinput, numi, space)
    wn = turtle.Screen()
    wn.exitonclick()

if __name__ == '__main__':
    main()
        





