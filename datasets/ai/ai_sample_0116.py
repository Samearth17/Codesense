import string
import random

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd_length = 8

    password = ''
    for i in range(pwd_length):
        password += random.choice(chars)
    
    # Check if at least one special character exists in the password
    if any([char in string.punctuation for char in password]):
        return password
    else:
        return generate_password()

print(generate_password())