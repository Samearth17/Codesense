import random

vowels = ['a', 'e', 'i', 'o', 'u']
constants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def generate_name():
    name = ""
    for _ in range(2):
        name += random.choice(constants).capitalize()
        for _ in range(2):
            name += random.choice(vowels)
        name += random.choice(constants)
    return name

print(generate_name())