import random
import string

def generate_password():
 letter_lowercase = string.ascii_lowercase
 letter_uppercase = string.ascii_uppercase
 numbers = string.digits
 symbols = string.punctuation
 all_chars = letter_lowercase + letter_uppercase + numbers + symbols
 
 password = ""
 
 for i in range(2):
     password += random.choice(letter_lowercase)
     password += random.choice(letter_uppercase)
     password += random.choice(numbers)
     password += random.choice(symbols)
 
 for i in range(2):
     password += random.choice(all_chars)
 
 password_list = list(password)
 random.shuffle(password_list)
 password = ''.join(password_list)
 
 return password