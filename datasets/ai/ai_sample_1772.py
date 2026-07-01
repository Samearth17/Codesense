def top_five(dict_list, key):
 sorted_list = sorted(dict_list, key=lambda k: k[key], reverse=True)
 return sorted_list[:5]
 
my_list = [
 {'name': 'Tom', 'score': 10},
 {'name': 'John', 'score': 20},
 {'name': 'Kate', 'score': 15},
 {'name': 'Bob', 'score': 17},
 {'name': 'David', 'score': 25},
 {'name': 'Carol', 'score': 8},
]
top_five_results = top_five(my_list, 'score')
print(top_five_results)

# Output: 
[{'name': 'David', 'score': 25}, {'name': 'John', 'score': 20}, {'name': 'Bob', 'score': 17}, {'name': 'Kate', 'score': 15}, {'name': 'Tom', 'score': 10}]