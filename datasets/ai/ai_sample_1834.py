import string
import random

def generate_password():
 chars = string.ascii_letters + string.digits + string.punctuation
 password = random.choice(string.ascii_lowercase)
 password += random.choice(string.ascii_uppercase)
 password += random.choice(string.digits)
 password += random.choice(string.punctuation)

 for i in range(4):
 password += random.choice(chars)

 passwordList = list(password) 
 random.SystemRandom().shuffle(passwordList) 
 password = ''.join(passwordList) 
 return password