string = "Hello World"

# get length of the string
length = len(string)

# create an empty string
reverse = ""

# loop backword through the string
for i in range(length-1, -1, -1):
 # add current character to empty string
 reverse = reverse + string[i]

# print out the result
print(reverse)