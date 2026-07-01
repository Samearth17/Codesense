def most_frequent_elements(lst):
 count = {}
 for item in lst:
 if item in count:
 count[item] += 1
 else:
 count[item] = 1
 max_count = 0
 max_element = None
 for item in count:
 if count[item] > max_count:
 max_count = count[item]
 max_element = item

return max_element

print(most_frequent_elements([3, 4, 2, 5, 4, 3, 2, 5, 4]))
# Output: 4