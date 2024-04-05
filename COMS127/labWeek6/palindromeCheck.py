# #    *                                                         
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
# 
# 
# Description: 



def main():
    import reverseString
    rs = reverseString
    user_input = str(input('Pick a string any string: '))
    def palindromeCheckV1(user_input):
        if user_input == rs.reverseStringV1(user_input):
            print('WOW, your input is a palindrome!!!')
        else:
            print('Wahh, Wahh, your input is not a palindrome.')
    def palindromeCheckV2(user_input):
        start = 0
        end = len(user_input) - 1
        while start < end:
            if user_input[start] != user_input[end]:
                print('Wahh, Wahh, your input is not a palindrome.')
                return False
                

            start += 1
            end -= 1
        print('WOW, your input is a palindrome!!!')
        return True
        
        


    print(palindromeCheckV1(user_input))
    print(palindromeCheckV2(user_input))



if __name__ == "__main__":
    main()
