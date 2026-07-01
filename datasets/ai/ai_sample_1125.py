# Initializing the list
list1 = [5, 6, 10, -9, 3, 21]

# Maximum and Minimum in a List

max = list1[0]
min = list1[0]

# Print all the list elements
for i in range(0, len(list1)):
    if list1[i]>max:
        max = list1[i]
    if list1[i]<min:
        min = list1[i]

print("The max value is:", max)
print("The min value is:", min)