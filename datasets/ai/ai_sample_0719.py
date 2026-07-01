string = input("enter a string")

# Create dictionary to keep track of count of characters 
d = {} 
  
# Loop through each character in string and add it to 
# dictionary as key and its count as value 
for char in string: 
    if char in d: 
        d[char] += 1
    else: 
        d[char] = 1
  
# Initialize min with the first characters frequency 
# and character with first character  
max_value = 0
max_char = string[0]
  
# Loop through each character in string  
for char in string: 
    val = d.get(char) 
    if val > max_value: 
        max_value = val 
        max_char = char
print("Character with maximum occurrence is: ", max_char)