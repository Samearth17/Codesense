import re

def validate_email(address):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, address):
        return True
    else:
        return False

def main():
    address = input('Enter email address: ')
    if validate_email(address):
        print("Valid email address")
    else:
        print("Invalid email address!")

main()