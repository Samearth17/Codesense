def find_sublists(my_list):
 # Initialize result 
 res = [[]]  
 # Consider each element of the original list  
 for elements in my_list: 
  # Initialize temp 
  temp = []  
  
  # Store current element in temp 
  temp.append(elements) 
  
  # For every element in the result, add the 
  # current element - temp 
  for r in res: 
   new_r = r + temp 
   res.append(new_r) 
   
  # Print the result 
  for r in res: 
   print(r)          

# Driver code 
my_list = [1, 2, 3, 4] 

find_sublists(my_list)