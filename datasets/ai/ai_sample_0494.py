import random

# Create an empty list
data = []

# Generate 20 names and ages
for i in range(20):
 name = 'Name ' + str(i)
 age = random.randint(18, 70)

# Append the data to the list
 data.append([name, age])

# Print out the list
print(data)

# [['Name 0', 64],
#  ['Name 1', 18],
#  ['Name 2', 24],
#  ['Name 3', 36],
#  ['Name 4', 34],
#  ['Name 5', 28],
#  ['Name 6', 56],
#  ['Name 7', 42],
#  ['Name 8', 68],
#  ['Name 9', 24],
#  ['Name 10', 50],
#  ['Name 11', 20],
#  ['Name 12', 54],
#  ['Name 13', 40],
#  ['Name 14', 61],
#  ['Name 15', 40],
#  ['Name 16', 41],
#  ['Name 17', 38],
#  ['Name 18', 56],
#  ['Name 19', 41]]