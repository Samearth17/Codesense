"""
Generate a new list containing the square of all numbers in a list
"""
# input list
in_list = [1,2,3,4,5]

# output list
out_list = []

# loop over the input list
for i in in_list:
    # calculate the square of the element and append it to output list
    out_list.append(i**2)

# print the output list
print(out_list)