def longest_subarray_with_sum(arr, given_sum):
  max_len = 0
  curr_sum = 0
  start_index = 0
  n = len(arr)
  for end_index in range(n):
    curr_sum += arr[end_index]
    while curr_sum > given_sum:
      curr_sum -= arr[start_index]
      start_index += 1
    if curr_sum == given_sum and (end_index-start_index+1) > max_len:
      max_len = end_index-start_index+1
  return max_len

arr = [1, 2, 3, 4, 5]
given_sum = 9
print(longest_subarray_with_sum(arr, given_sum))