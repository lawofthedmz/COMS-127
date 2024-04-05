#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
#  Murphy Glawe             10/4/2023
# 
#           [COMS 127 Section 6]
#  LabWeek 7
#
#
# Description: a program that takes a randomly generated list full of random integers and finds the mean and median and prints to user 
import random

def generateInput(): # generates random list used in rest of program 
    numbers = []
    elements_inList = random.randint(200, 500)
    while elements_inList > 0:
        numberToList = random.randint(1, 2000)
        numbers.append(numberToList)
        elements_inList -= 1
    return numbers

def findMean(numlist): # mean formula citation: https://www.cuemath.com/data/mean/
    start = 0
    end = len(numlist)
    numsum = 0 
    print(numlist[start])
    while start < end:
        numsum += numlist[start]
        start += 1
    mean = numsum/end
    return mean

def findMedian(numlist):
    numlist.sort()
    length = len(numlist)
    if length % 2 == 1:
        return numlist[length // 2]
    else:
        middle1st = numlist[length // 2 - 1]
        middle2nd = numlist[length // 2]
        return (middle1st + middle2nd) / 2



def main():
    stats_list = generateInput()
    mean = findMean(stats_list)
    median = findMedian(stats_list)
    print(f"Your list has a mean of {mean} and a median of {median}.")

if __name__ == "__main__":
    main()
