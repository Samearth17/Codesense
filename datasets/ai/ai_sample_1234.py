"""
Write a code to find the longest word in an array of strings

"""

mywords = ["Hello", "World", "Python", "Programming"]

#Set a variable to hold the longest word
longest_word = ''

#Loop through the array of strings
for word in mywords:
    #Compare the length of the current word with the longest word
    if len(word) > len(longest_word):
        #Replace the longest_word variable with the new longest word
        longest_word = word

#Print out the result
print("The longest word is " + longest_word)