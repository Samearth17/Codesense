def findMaxLen(listA, listB):
  lengthA = len(listA)
  lengthB = len(listB) 
  
  # Initialize left and right pointers 
  l, r = 0, 0
  
  max_len = 0 
  
  # While left and right pointer cross the other    
  # maintain a maximum length
  while l < lengthA and r < lengthB: 
      # If they both have same element 
      if listA[l] == listB[r]:
          max_len = max(max_len, l + r + 1) 
          l += 1
          r += 1
      
      # If listA's element is less, increment  
      # listB pointer 
      elif listA[l] > listB[r]:
          r += 1
          
      # If listA's element is more, increment  
      # listA pointer
      else:
          l += 1   
  return max_len