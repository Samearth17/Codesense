import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password_length = 8
    password = ""

    for i in range(password_length):
        index = random.randint(0, len(characters) - 1)
        password += characters[index]

    if not any(char.islower() for char in password):
        password = password[:7] + random.choice(string.ascii_lowercase)

    if not any(char.isupper() for char in password):
        password = password[:7] + random.choice(string.ascii_uppercase)

    if not any(char.isdigit() for char in password):
        password = password[:7] + random.choice(string.digits)
    
    return password

print(generate_password())