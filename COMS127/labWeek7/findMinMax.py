#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
#  Murphy Glawe             10/2/2023
# 
#           [COMS 127 Section 6]
#  LabWeek 7
# Citations:::  https://runestone.academy/ns/books/published/thinkcspy/Lists/TuplesasReturnValues.html?mode=browsing     accessed 10/2/2023 
#
#
# Description: a program that takes user integer inputs and adds them to a list then finds the minninum and maximum of the list 
def take_input():
    numbers = []
    while True:
        user_input = input("Enter an integer or press [*] to stop: ")
        if user_input == '*':
            break
        if user_input.isdigit(): # .isdigit checks if value is of numeric value if not it returns false 
            numbers.append(user_input)
        else:
            print("Invalid Input please enter proper integer!")
    return numbers

def findMin(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min 
def findMax(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max



    

def convert_integers(numbers):
    return [int(num) for num in numbers]
    


def main():
    user_input = take_input()
    converted_numbers =  convert_integers(user_input)

    if not converted_numbers:
        print("No numbers were entered dude.")
    else:
        print(f"You entered numbers are {converted_numbers}.")
        min_number = findMin(converted_numbers)
        print(f"Your mininum number is {min_number}.")

        max_number = findMax(converted_numbers)
        print(f"Your max number is {max_number}.")
    
if __name__ == "__main__":
    main()

