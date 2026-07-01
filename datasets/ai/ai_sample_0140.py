import string
import random

# length of password
length = 8

# special characters
special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# generating password
password = random.choice(string.ascii_lowercase)
password += random.choice(string.ascii_uppercase)
password += random.choice(string.digits)
password += random.choice(special_characters)

for i in range(length):
   password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + special_characters)

password  = ''.join(random.sample(password,len(password)))

print ("Password is: ", password)