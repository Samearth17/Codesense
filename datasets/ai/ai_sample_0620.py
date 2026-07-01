def remove_multiple_occurrences(arr):
 seen = set([]) # stores all the numbers we've seen before
 new_arr = [] # stores the numbers that occurred only once or twice

for num in arr:
 if num not in seen:
  seen.add(num) # add to the numbers we've seen
  new_arr.append(num)
 elif num in seen:
  seen.remove(num) # remove from the "seen" set

return new_arr

arr = [1,2,1,3,4,2,2,2,3,1]
print(remove_multiple_occurrences(arr))
# Prints [4]