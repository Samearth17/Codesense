# Python program to generate 
# a unique 6 digit number 
import random 
def generate_number(): 
      
    # Choose a random number 
    # between 10000 and 99999 
    random_number = random.randint(10000, 99999) 
  
    # Return the random number 
    return random_number 
  
# Driver Code 
if __name__ == "__main__": 
    print(generate_number())