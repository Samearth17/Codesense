import string 
import random

def generate_password(length): 
    password = "" 
    for i in range(length): 
        character = random.choice(
            string.ascii_letters + 
            string.digits + 
            string.punctuation)
        password += character
    return password

password = generate_password(10) 
print(password)