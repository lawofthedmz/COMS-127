# Murphy Glawe          9/20/2023
#  
# Lab Week 5        [COM S 127 SECTION 6]
#
#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠒⠒⠒⠒⠒⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⡰⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠙⠄⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⢠⠂⠀⠀⠘⡄⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⢤⡀⢂⠀⢨⠀⢀⡠⠈⢣⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⢀⢀⡖⠒⠶⠤⠭⢽⣟⣗⠲⠖⠺⣖⣴⣆⡤⠤⠤⠼⡄⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠘⡈⠃⠀⠀⠀⠘⣺⡟⢻⠻⡆⠀⡏⠀⡸⣿⢿⢞⠄⡇⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⢣⡀⠤⡀⡀⡔⠉⣏⡿⠛⠓⠊⠁⠀⢎⠛⡗⡗⢳⡏⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⢱⠀⠨⡇⠃⠀⢻⠁⡔⢡⠒⢀⠀⠀⡅⢹⣿⢨⠇⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⢸⠀⠠⢼⠀⠀⡎⡜⠒⢀⠭⡖⡤⢭⣱⢸⢙⠆⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠸⢁⡀⠿⠈⠂⣿⣿⣿⣿⣿⡏⡍⡏⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠸⢢⣫⢀⠘⣿⣿⡿⠏⣼⡏⠀⠀⠀⠀⠀⠀⠀")
print(" ⠀⠀⠀⠀⣀⣠⠊⠀⣀⠎⠁⠀⠀⠀⠙⠳⢴⡦⡴⢶⣞⣁⣀⣀⡀⠀⠀⠀⠀⠀")
print(" ⠀⠐⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢀⠤⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀")                                                                                       

import myShapes
import myTemps
print("Murphy Glawe         9/20/2023")
print()
print("[LAB WEEK 5 SECTION 6]       [COMS 127 SECTION J]")
print()




def userinput():
    i = int(input('Pick an integer: '))
    return i 


##----------------------------------------------------------------------------------------------------------------------------------------------------
# function that allows user to pick between the calculation functions imported from myShapes.py and my.Temps.py and returns a answer
def main():
    running = True
    while running:
        userchoice = input('Choose which program to run: [S]hape Calculations, [T]emp Calculations, or [Q]uit: ')
        if userchoice == 'S':
            shape_calculation = input('What shape calculation would you like to perform: [1]Cube Surface, [2]Cube Volume, [3]Sphere Surface, or [4]Sphere Volume: ')
            if shape_calculation == '1':
                ans = myShapes.cubeSurface(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif shape_calculation =='2':
                ans = myShapes.cubeVolume(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif shape_calculation == '3':
                ans = myShapes.sphereSurface(userinput())
                print(f"The answer to your calculatioin is {ans}") 
            elif shape_calculation == '4': 
                ans = myShapes.sphereVolume(userinput())                  
                print(f"The answer to your calculatioin is {ans}")
            else:
                ans = print("ERROR ERROR ERROR! Please pick one of the calculations")
        elif userchoice == 'T':
            temp_calculation = input('What temperature calculation would you like to perform: [1]Celsius to Fahrenheit, [2]Celsius to Kelvin, [3]Fahrenheit To Celsius, [4]Fahrenheit To Kelvin, [5]Kelvin To Celsius, or [6]Kelvin To Fahrenheit: ')   
            if temp_calculation == '1':
                ans = myTemps.celsiusToFahrenheit(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif temp_calculation == '2':
                ans = myTemps.celsiusToKelvin(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif temp_calculation =='3':
                ans = myTemps.fahrenheitToCelsius(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif temp_calculation == '4':
                ans = myTemps.fahrenheitToKelvin(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif temp_calculation == '5':
                ans = myTemps.kelvinToCelsius(userinput())
                print(f"The answer to your calculatioin is {ans}")
            elif temp_calculation == '6':
                ans = myTemps.kelvinToFahrenheit(userinput())
                print(f"The answer to your calculatioin is {ans}")
            else:
                print("ERROR ERROR ERROR! Please pick one of the calculations")
            
        elif userchoice == 'Q':
            running = False
            print('See you later!')
            

            
# keeps program running unitl user [q]uits

if __name__ == "__main__":
    main()
      



    


