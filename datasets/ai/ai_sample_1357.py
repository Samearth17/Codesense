def count_string_values(my_dict):
     count = 0
     for key, value in my_dict.items():
         if isinstance(value, str):
             count += 1
     return count
 
my_dict = {
    "name": "John Smith",
    "age": 30,
    "gender": "Male",
    "is_ married": True
}

# Count number of string values
result = count_string_values(my_dict)

print(result)