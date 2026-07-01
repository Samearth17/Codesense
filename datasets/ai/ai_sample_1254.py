my_string = "Python is an interesting language"

# create an empty dictionary
di = {}

# iterate through each character
for char in my_string:
    # check if the character is already present in the dict
    if char in di.keys():
        # if present, increment the value of the character
        di[char] += 1
    else:
        # if not present, set the value to 1
        di[char] = 1

# find the character with the maximum count
max_char = max(di, key=di.get)

# display the maximum occurring character
print(f"Maximum occurring character is: {max_char}")