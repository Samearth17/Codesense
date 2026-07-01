series = [1, 4, 5, 7]

# count even and odd numbers
even_count = 0
odd_count = 0

for num in series:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the total number of even and odd numbers
print('Number of even numbers: {}'.format(even_count))
print('Number of odd numbers: {}'.format(odd_count))