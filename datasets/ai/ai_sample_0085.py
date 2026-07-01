import re 
  
# input string 
strings = ["First","Second","Third"]

# Get the string 
inp_str = input("Please enter your string :") 

# Initialize the flag 
found = False
  
# Search the string 
for i in strings: 
    if re.search(i, inp_str):
        found = True

# Print result 
if found == True: 
    print("String matches") 
else: 
    print("String doesn't matches")