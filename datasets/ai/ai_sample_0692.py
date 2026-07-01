def merge_lists(a, b):
  merged_list = []
  a_pos = 0
  b_pos = 0
  
  while a_pos < len(a) and b_pos < len(b):
    if a[a_pos] < b[b_pos]:
      merged_list.append(a[a_pos])
      a_pos += 1
    else:
      merged_list.append(b[b_pos])
      b_pos += 1

  return merged_list + a[a_pos:] + b[b_pos:]

a = [1,3,5]
b = [2,4,6]
print(merge_lists(a,b))