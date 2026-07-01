import random 
  
# Function to scramble a given word 
def scramble(word):  
    # Define all the possible chars in the word 
    chars = list(word)  
  
    # Get a random permutation of the characters 
    random.shuffle(chars) 
  
    # Construct the scrambled word 
    scramble_word = ''.join(chars)  
  
    return scramble_word 

# Driver code 
word = 'listen'
scrambled = scramble(word) 
  
print(word + " scrambled becomes: " + scrambled)