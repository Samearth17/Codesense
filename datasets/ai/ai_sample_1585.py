def print_ascii(text):
    '''This function will print a given string with each character's ASCII code.'''
    for ch in text:
        print(f'{ch} : {ord(ch)}')

print_ascii('Hello world!')

# Output:
# H : 72
# e : 101
# l : 108
# l : 108
# o : 111
#  : 32
# w : 119
# o : 111
# r : 114
# l : 108
# d : 100
# ! : 33