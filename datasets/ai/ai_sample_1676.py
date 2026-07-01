# Python program to align text cells in a table to the left,he right, and center 

table = [('Name', 'Age', 'Gender'),
         ('John', '21', 'Male'),
         ('Doe', '25', 'Female')]

for row in table:
    # Align text to the left 
    left_aligned = "{:<10}{:<10}{:<10}".format(*row)  
    
    # Align text to the right
    right_aligned = "{:>10}{:>10}{:>10}".format(*row) 
    
    # Align text to the center
    center_aligned = "{:^10}{:^10}{:^10}".format(*row) 

print("Left aligned:")
print(left_aligned) 

print("Right aligned:")
print(right_aligned)

print("Center aligned:")
print(center_aligned) 

# Output:
# Left aligned:
# Name      Age       Gender    
# John      21        Male      
# Doe       25        Female  

# Right aligned:
#      Name      Age      Gender
#      John       21       Male
#      Doe        25       Female  

# Center aligned:
#    Name     Age     Gender  
#    John      21      Male    
#    Doe       25      Female