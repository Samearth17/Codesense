def is_valid_password(password): 
    if len(password) < 8: 
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for i in range(len(password)): 
        ch = password[i] 
        if ch.isupper(): 
            has_uppercase = True
        elif ch.islower():
            has_lowercase = True 
        elif ch.isdigit(): 
            has_digit = True

    if has_uppercase and has_lowercase and has_digit:  
        return True

    return False