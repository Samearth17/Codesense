my_string = "This is the string which is to be sorted"
  
words = my_string.split(' ') # split string into list of words 
  
# create a list of tuples where the first element 
# is the length of the word and the second element 
# is the word itself  
words_with_length = [(len(word), word) for word in words] 
  
# sort list of tuples according to 1st element of tuple i.e. length of word 
words_with_length.sort(reverse = True) 
  
# wl contains list words in decreasing order of their length 
# now use join() to join all words whith " " 
sorted_string = " ".join([i[1] for i in words_with_length]) 
  
# print sorted string 
print(sorted_string)