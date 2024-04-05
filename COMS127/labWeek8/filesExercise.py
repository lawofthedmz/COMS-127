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
# Description:  a Python script which makes all necessary calculations to produce the grades.txt file
def calculate_grades(students_file, scores_file, output_file):
   student_scores = []
   students_list = []
   with open(students_file, 'r') as students_data: # read student data from student.txt
    lines = students_data.readlines()
    lines = lines[1:]

    
    for line in lines:
      line = line.split(',')
      for i in range(0, len(line)):
        line[i] = line[i].strip()
  
      students_list.append(line)
    
    
# reads score file and combines names and scores into a list in order to calculate
    with open(scores_file, 'r') as scores_data: 
      lines = scores_data.readlines()
      
      lines = lines[1:] #skips first row containing header
      
      for line in lines:
        student_id, assignment, score = line.strip().split(',') # goes the scores_file line by line and assigns variables before between and after the two commas
        for i in range(0, len(students_list)):                  # to id, assignmnet and score  example var1,(SPLIT) var2,(SPLIT) var3
          if students_list[i][0] == student_id:
            students_list[i].append(assignment)
            students_list[i].append(int(score))
      
                                         

    # calcutlates score and adds to score list 
    for student in students_list: # goes through each unique student list which consists of (ids, names, assignments, score) and finds total scores and sum of scores for each student and appends to new list
      student_id = student[0]
      student_name = student[1]
      scores = [num for num in student if isinstance(num, int)] # sorts list of numbers and finds scores bc score is only integer
      total_scores = len(scores)
      sum_of_scores = sum(scores)
      if total_scores > 0:
        average = sum_of_scores/total_scores
      else:
        average = 0 
      student_scores.append([student_id, student_name, total_scores, sum_of_scores, average])

    
    

# creates output file and inputs students score 
    with open(output_file, 'w') as output:
      output.write('Student ID2, Name, Total Scores, Sum of all Scores, Score Average\n') # prints title on grades.txt
      for student in student_scores: # for index in the student scores list
        output.write(f"{student[0]}, {student[1]}, {student[2]}, {student[3]}, {student[4]}\n") # prints each each index in scores list and has a newline character after printing
      output.write("""

                              *                                                         
                            (  `                     )       (      (                   
                            )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
                          ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
                          (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
                          |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
                          | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
                          |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  


""")
      

      
     


if __name__ == "__main__":
   students_file = 'students.txt'
   scores_file = 'scores.txt' 
   output_file = 'grades.txt'

   calculate_grades(students_file, scores_file, output_file)