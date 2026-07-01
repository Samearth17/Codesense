def is_isbn_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
 
    sum = 0
    factor = 10
 
    for i in range(len(isbn)):
        if isbn[i].isdigit():
            sum += int(isbn[i]) * factor
        elif isbn[i].upper() == 'X':
            sum += 10 * factor
        else:
            return False
        factor -= 1
    
    if sum % 11 == 0:
        return True
    else:
        return False