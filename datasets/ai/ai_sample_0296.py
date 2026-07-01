import re

def check_password_strength(password):
    '''This function checks if the given password is strong according to NIST guidelines'''
    # check if password is atleast 8 characters long
    if len(password) < 8:
        return False
    
    # check if password contains atleast one lowercase letter
    if not re.search('[a-z]', password):
        return False
    
    # check if password contains atleast one uppercase letter
    if not re.search('[A-Z]', password):
        return False
    
    # check if password contains atleast one number
    if not re.search('[0-9]', password):
        return False
    
    return True