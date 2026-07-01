import string
import random

def generate_password():
    # Generate a password with at least 8 characters
    length = 8
    # Generate the password with at least one lower, one upper and one non-alphanumeric character
    password = ''.join(
        random.choice(
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits +
            string.punctuation
        ) for i in range(length)
    )
    print(password)

if __name__ == '__main__':
    generate_password()