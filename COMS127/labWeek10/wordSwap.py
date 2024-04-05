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
# Description:  a Python that takes user input for an entire sentence and swaps word within the sentence 
import random 

def wordswap(sentence):
    # splits 'sentence' into individual words
    list_of_words = sentence.split() 
    # creates a dictionary to store the 'replacements' of each word
    sentence_and_replacements = {}
    new_sentence = []
    # for loop that iterates through 'list_of_words' 
    for word in list_of_words:
        # assigns the key a random word(from 'list_of_words') if the word is not already in the dictionary
        if word not in sentence_and_replacements:
            random_word = random.choice(list_of_words)
            sentence_and_replacements[word] = random_word
    
    for word in list_of_words:
        new_sentence.append(sentence_and_replacements[word])
    
    new_sentence = " ".join(new_sentence)
    

    
    print(sentence_and_replacements)
    print(new_sentence)

# calls main fucntion 
if __name__ == "__main__":
    # gathers a sentence as input
    sentence = input("Please type a sentence: ")
    wordswap(sentence)