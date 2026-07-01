def sort_dict_by_key(dictionary):
 sorted_list = []
 for key in sorted(dictionary):
 sorted_list.append(dictionary[key])
 return sorted_list

# Example
mydict = {
 'John': 23,
 'Alice': 27,
 'Bob': 17,
 'Eve': 33
}

print(sort_dict_by_key(mydict))
# Output: [17, 23, 27,33]