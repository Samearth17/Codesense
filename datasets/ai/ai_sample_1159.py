def split_array_sum(arr):
  sum_arr = sum(arr)
  half_sum = sum_arr // 2
  current_sum = 0
  left_index = 0
  
  for index, value in enumerate(arr):
    current_sum += value
    if current_sum >= half_sum:
        left_index = index
        break
  
  left_arr = arr[:left_index+1]
  right_arr = arr[left_index+1:]
  return left_arr, right_arr