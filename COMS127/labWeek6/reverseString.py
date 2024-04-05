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
#
# Description: a main funciton that takes a user string input and reverses it using two different functions
# one being the backwards step slice and the other using a character addition for loop
def reverseStringV1(user_string):
        reversed_string = user_string[::-1]
        return reversed_string
# def reverseStringV2(user_string):
#     reversed_string = ""
#     for char in user_string:
#         reversed_string = char + reversed_string
#         return reversed_string

def main():
    user_string = str(input("Pick a string any string: "))
    print(reverseStringV1(user_string))
    # print(reverseStringV2(user_string))
        










if __name__ == "__main__":
    main()