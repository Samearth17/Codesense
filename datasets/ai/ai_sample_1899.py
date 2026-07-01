total_age = 0

# open and read the file
with open('student.csv', 'r') as f:
    # read the file
    data = f.read().splitlines()

# loop through the rows
for row in data:
    # get the age from each row
    age = row.split(',')[1]
    # add the age to the total
    total_age = total_age + int(age)

# calculate the average age of all the students
avg_age = total_age / len(data)

# print the result
print('Average age of all students is: ', avg_age)