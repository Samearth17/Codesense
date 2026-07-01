def check_type(str):
    try:
        int(str)
        return 'Integer'
    except ValueError:
        pass
   
    try:
        float(str)
        return 'Float'
    except ValueError:
        pass
   
    return 'String'

print(check_type('123')) # prints 'Integer'