# Murphy Glawe          10/31/2023
#
#   Lab Week 11   [COM S 127 Section 6]
#
# 
# 
# Description: recursuve functon that has a value n and a goal, prints call stack valuse until reaching goal then does the oppisite for the reversed function 

def countDownGoalRecursive(n, goal):
    if n < goal:
        return
    else: 
        print(n)
        countDownGoalRecursive(n-1, goal)

def countDownGoalRecursiveReversed(n, goal):
    if n < goal:
        return
    else: 
        countDownGoalRecursiveReversed(n-1, goal)
        print(n)        


def main():
    countDownGoalRecursive(5, 3)
    print("\n")
    countDownGoalRecursiveReversed(5,3)




if __name__ == "__main__":
    main()