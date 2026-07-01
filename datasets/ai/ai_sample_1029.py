data = [1, 10, 3, 11, 7, 8, 4, 2]

max_sequence = 0
curr_sequence = 0
prev = -1

for num in data:
    # Check if the current number is larger than the previous one
    if num > prev:
        curr_sequence += 1
        max_sequence = max(max_sequence, curr_sequence)
    else:  # Reset the length of the current sequence to 1
        curr_sequence = 0

print(max_sequence)  # Output 3