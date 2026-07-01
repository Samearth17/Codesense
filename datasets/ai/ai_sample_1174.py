def num_to_month(num):
    months = [
        'January', 
        'February', 
        'March', 
        'April', 
        'May', 
        'June', 
        'July', 
        'August', 
        'September', 
        'October', 
        'November', 
        'December'
    ]
    return months[num - 1]

print(num_to_month(2)) # February