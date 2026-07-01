import random

numbers = []
total = 0

#Generate 10 random numbers
for i in range(10):
    n = random.randint(0, 100)
    numbers.append(n)
    total += n

#Print the generated numbers
print("Generated numbers :")
for i in numbers:
    print(i)

#Calculate and print the average
average = total / len(numbers)
print("The average is:", average)