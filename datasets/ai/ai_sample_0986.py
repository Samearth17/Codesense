# Python 3 program to print the list of words and their scores 
# sorted in descending order of scores

# function is used to sort the list of words
# according to the scores in decreasing order
def sort_list(list): 
    sorted_list = sorted(list, key=lambda x: x[1], reverse = True) 
    return sorted_list 
  
# Driver code 
scores = {"cat": 5, "dog": 2, "elephant": 7, "tiger": 3}

# Creating a list of tuples and sorting them 
list = [] 
for word, score in scores.items(): 
    list.append((word, score)) 
   
# Printing the modified list 
sorted_list = sort_list(list) 

for word,score in sorted_list:
    print("Word: {0}, Score: {1}".format(word, score))