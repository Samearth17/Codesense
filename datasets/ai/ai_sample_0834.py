import random
import string

def generate_password(length, complexity):
    # minimum 8 characters
    if length < 8:
        length = 8
    # maximum complexity 5
    if complexity > 5:
        complexity = 5

    char = string.ascii_letters + string.digits + string.punctuation
    pwd = []
    while len(pwd) < length:
        char_rand = random.choice(char)
        if char_rand not in pwd:
            pwd.append(char_rand)

    random.shuffle(pwd)
    return ''.join(pwd[:length])

print(generate_password(20,5))