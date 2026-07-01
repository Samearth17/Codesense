def multi_sort(lst, keys): 
    # lst is a list of dictionaries
    # keys is a list containing the keys to sort on
    split_list = [item[k] for k in keys] 
    lst.sort(key = lambda x:split_list) 
    return lst 

# Example:
my_list = [{"name": "John", "age": 24}, 
           {"name": "Chris", "age": 25},
           {"name": "John", "age": 20}] 
keys = ["name", "age"]
  
multi_sort(my_list, keys)

# Output:
[{'name': 'Chris', 'age': 25}, 
 {'name': 'John', 'age': 20}, 
 {'name': 'John', 'age': 24}]