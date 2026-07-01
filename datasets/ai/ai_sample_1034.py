# Set up an empty dictionary
# to store the frequencies of strings
string_freq = {}

# Iterate the list of strings
for string in list_of_strings:
  # If the string is already in 
  # the dictionary, increment its frequency
  if string in string_freq:
    string_freq[string] += 1
  else:
    # If the string is not in the 
    # dictionary, initialise its frequency
    string_freq[string] = 1

# Print the frequencies of the strings
for string,freq in string_freq.items():
  print(string + ": " + str(freq) + " times")