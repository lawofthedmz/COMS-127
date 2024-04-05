#    *                                                         
#  (  `                     )       (      (                   
#  )\))(    (  (         ( /((      )\ )   )\   ) (  (     (   
# ((_)()\  ))\ )(  `  )  )\())\ )  (()/(  ((_| /( )\))(   ))\  
# (_()((_)/((_|()\ /(/( ((_)(()/(   /(_))_ _ )(_)|(_)()\ /((_) 
# |  \/  (_))( ((_|(_)_\| |(_)(_)) (_)) __| ((_)__(()((_|_))   
# | |\/| | || | '_| '_ \) ' \ || |   | (_ | / _` \ V  V / -_)  
# |_|  |_|\_,_|_| | .__/|_||_\_, |    \___|_\__,_|\_/\_/\___|  
#                 |_|        |__/                         
#  Murphy Glawe             10/23/2023
# 
#           [COMS 127 Section 6]
#  LabWeek 10
# 
# Description:
def analyzeBook(f):
    try:
        count = {}
        with open(f + '.txt', 'r') as f:
            for line in f:
                for word in line.split():
                
                # remove punctuation
                    word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                    word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                    word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                    word = word.replace(']', '').replace(';', '')
                    
                    # ignore case
                    word = word.lower()
                    
                    # ignore numbers
                    if word.isalpha():
                        if word in count:
                            count[word] = count[word] + 1
                        else:
                            count[word] = 1
        return count
    except FileNotFoundError:
        print(f'File "{f}.txt" not found')
         

def outputAnalysis(count, book_file):
    try:
        with open(book_file + '_analysis.txt', 'w') as out:

            keys = list(count.keys())
            keys.sort()

            for word in keys:
                out.write(word + " " + str(count[word]))
                out.write('\n')
        return True
    except:
        print('An error occurred while writing this file.')
        return False



def main():
    f = input('Input file: ') # input for file name 
    
    count = analyzeBook(f)
    
    if count is not None:
        if outputAnalysis(count, f):
            print(f'Analysis saved as {f}_analysis.txt.')
        else:
            print("An error occured while saving your analysis file.")
    









if __name__ == "__main__":
    main()