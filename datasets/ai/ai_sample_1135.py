def most_frequent(list):
 max_count = 0
 max_item = None
 dict = {} 
 for item in list: 
  if (item in dict):  
    dict[item] += 1
  else:
    dict[item] = 1
 
 for key, value in dict.items(): 
  if value > max_count: 
    max_count = value
    max_item = key
 
 return max_item

list = [2,2,2,3,3,3,4,6,7,6]
print(most_frequent(list))