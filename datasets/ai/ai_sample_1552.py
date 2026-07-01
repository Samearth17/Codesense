def sortDict(dictionary):
 # Sort the keys.
 sorted_keys = sorted(dictionary.keys())
 # Initialize a new dictionary with the sorted keys.
 sorted_dict = dict.fromkeys(sorted_keys)
 # Assign values from the original dictionary to the sorted dictionary.
 for key in sorted_dict:
 sorted_dict[key] = dictionary[key]
 # Return the sorted dictionary.
 return sorted_dict

dictionary = {
 'Tom': 20,
 'Jerry': 30,
 'Jose': 25
}

print(sortDict(dictionary)) # {'Jose': 25, 'Jerry': 30, 'Tom': 20}