def find_element(my_list, x):
  found = False
  for item in my_list:
    if item == x:
      found = True
      break
  
  return found

element = 3

print(find_element(my_list, element))

# Output
True