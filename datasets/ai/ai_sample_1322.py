# Python Program to find out the 
# frequency of each character in a string 
  
# defining a string 
str1 = "Hello World"
  
# creating an empty dictionary 
all_freq = {} 
  
# loop to find all frequencies of  
# each character in string 
for i in str1: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
# printing result 
print("Count of all characters in the given string is :\n "
                                        +  str(all_freq))