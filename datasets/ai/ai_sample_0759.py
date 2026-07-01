import string
import random
  
def genPassword(length): 
    # Create strings of possible characters 
    digits = string.digits
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    all = upper + lower + digits + special
  
    # Create empty strings 
    password = ''
    upper_password = ''
    lower_password = ''
    digit_password = ''
    special_password = ''
  
    # Iterate a loop over given length of string and all character array to generate random password with given rules
    for x in range(length):
        upper_password = upper_password + random.choice(upper)
        lower_password = lower_password + random.choice(lower)
        digit_password = digit_password + random.choice(digits)
        special_password = special_password + random.choice(special)
    
    # Concate all character string to generate random password
    password = upper_password + lower_password + digit_password + special_password
    # Use 'sample' method to scatter characters in password string
    password = ''.join(random.sample(password, len(password))) 
  
    return password 
  
length = 12
password = genPassword(length)
print(password)