import string 
import random 

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    if (any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in string.punctuation for c in password)):
       return password
    else:
       return generate_password(length)
  
# Create random passwords with length 10 
x = generate_password(10) 
print ('Random Password :', x)