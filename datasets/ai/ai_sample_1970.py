def determine_grade(marks):
    # Determine the average mark
    avg = (marks['math'] + marks['history'] + marks['english'])/3
    
    # If the average mark is greater than or equal to 90, the student's grade is A 
    if avg >= 90:
        return 'A'
    # If the average mark is greater than or equal to 80, the student's grade is B 
    elif avg >= 80:
        return 'B'
    # If the average mark is greater than or equal to 70, the student's grade is C 
    elif avg >= 70:
        return 'C'
    # If the average mark is greater than or equal to 60, the student's grade is D 
    elif avg >= 60:
        return 'D'
    # Anything less than 60 is an F 
    else:
        return 'F'