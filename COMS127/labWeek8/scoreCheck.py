#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
#  Murphy Glawe             10/10/2023
# 
#           [COMS 127 Section 6]
#  LabWeek 8
# 
# Description: a program that takes input from a user to determine a threshold value then prints out how many scores the people from the txt file have above and below the threshold
def process_data(file_name, threshold):
    file_contents = open(file_name, 'r')
    for line in file_contents:
        content = line.split()
        student = content[0]
        scores = [int(line) for line in content[1:]]
        above = sum(line >= threshold for line in scores)
        below = sum(line < threshold for line in scores)
        print(f"{student} has {above} above threshold scores and {below} scores below.")
        
if __name__ == "__main__":
    file_name = "studentData.txt"
    threshold = int(input("Please enter the threshold value: "))
    process_data(file_name, threshold)
    