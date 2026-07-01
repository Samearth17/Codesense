import random

def scrambleString(string):
  # Split the string into a list
  chars = list(string)

  # Shuffle the list
  random.shuffle(chars)

  # Join the list to form the scrambled string
  scrambled = "".join(chars)

  return scrambled

# Create the string
string = "Hello World"

# Scramble the string
scrambled = scrambleString(string)

# Print the result
print(scrambled)