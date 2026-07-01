import random
import string

def generate_random_password():
  # Choose a length for the password
  length = 8
  
  # Create the password
  password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
  
  print("Generated Password:", password)
  
  return password

generate_random_password()