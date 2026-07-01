string = "Lorem ipsum dolor sit amet consectetur adipiscing elit morbi in ultrices"

# Create an empty dictionary  
freq = {} 
  
# Loop through the string and populate the dictionary  
for i in string:
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1

# Get the most frequently occurring character 
max_freq = 0
for key, value in freq.items(): 
    if value > max_freq: 
        max_freq = value 
        max_char = key

# Print the most frequent character  
print("The most frequent character is '" + max_char + "' and it occurred " + str(max_freq) + " times.")