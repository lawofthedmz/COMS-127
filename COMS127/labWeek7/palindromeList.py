#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
#  Murphy Glawe             10/3/2023
# 
#           [COMS 127 Section 6]
#  LabWeek 7
#
#
# Description: a program that takes user input of strings and adds them to a list, the list is checked if it is paldromic and the result is returned to the user 

def take_input():
    user_words = []
    while True: 
        user_input = input("Please enter words, press [*] to stop: ")
        test = isinstance(user_input, str)
        if user_input == '*':
            break
        if test == True: 
            user_words.append(user_input)
        else:
            print("Invalid input please enter proper string!")
    return user_words

def palindromeCheck(user_input):
        start = 0
        end = len(user_input) - 1
        while start < end:
            if user_input[start] != user_input[end]:
                prompt = ("not palindromic")
            else: 
                prompt = ("palindromic")
                
            return prompt


def palindromeList(palindrome_list):
    checked_list = palindromeCheck(palindrome_list)
    return checked_list
    
def main():
    user_list = take_input()
    checked_list = palindromeList(user_list)

    
    print(f"Your list: {user_list} is {checked_list}.")


if __name__ == "__main__":
    main()