def find_longest_increasing_sequence(arr):
 longest_start = 0
 longest_length = 0

 current_start = 0
 current_length = 0

 for i in range(1, len(arr)):
 prev_val = arr[i - 1]
 curr_val = arr[i]

 if curr_val > prev_val:
 current_length += 1
 else:
 current_start = i
 current_length = 1

 if current_length > longest_length:
 longest_start = current_start
 longest_length = current_length

 longest_sequence = arr[longest_start:longest_start + longest_length]
 return longest_sequence

arr = [3, 2, 1, 4, 5, 6, 7, 8]
longest_seq = find_longest_increasing_sequence(arr)
print(longest_seq) // Output: [4, 5, 6, 7, 8]