import random

# define the size of the array
x, y = 10, 10

# create an empty array of the given size
arr = [[0 for j in range(x)] for i in range(y)]

# fill the array with random numbers
for i in range(x):
 for j in range(y):
 arr[i][j] = random.randint(0, 9)

# print the array
for i in range(x):
 print(arr[i])