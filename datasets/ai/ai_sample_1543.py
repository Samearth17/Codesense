import re

def validate_password(password):
    # password should be at least 8 characters
    if len(password) < 8:
        return False
 
    # password should have at least one number
    if re.search('[0-9]', password) is None:
        return False
 
    # password should have at least one uppercase
    if re.search('[A-Z]', password) is None:
        return False
 
    # password should have at least one lowercase
    if re.search('[a-z]', password) is None:
        return False
 
    return True