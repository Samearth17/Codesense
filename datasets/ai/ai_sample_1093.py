def generate_alternating_2d_array(n):
 arr = []
 prev_value = False
 for i in range(n):
  row = []
  for j in range(n):
   cur_value = not prev_value
   row.append(cur_value)
   prev_value = cur_value 
  arr.append(row)
 return arr

arr = generate_alternating_2d_array(5)
for row in arr:
 print(row)