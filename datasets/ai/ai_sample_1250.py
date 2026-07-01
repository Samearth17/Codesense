"""
Create a method in Python which prints the frequency of each letter in a string
"""

# Function to print frequency of characters in a string  
def characterFrequency(text): 
    count = [0 for i in range(256)] 
    output = [] 
  
    # count frequency of each character  
    # in string 
    for i in range(len(text)):  
        count[ord(text[i])] += 1
  
    # Print characters and their frequencies 
    for i in range(len(count)): 
        if count[i] > 0: 
            output.append((chr(i), count[i]))
    output.sort(key=lambda x:x[1], reverse=True)
    
    for i in output: 
        print(i[0], '-', i[1])
  
# Driver code
text = "hello world"
characterFrequency(text)

# Output:
# l - 3
# o - 2
# h - 1
# e - 1
# d - 1
# r - 1
# w - 1