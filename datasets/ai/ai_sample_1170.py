employees.sort(key=lambda x: x['salary'], reverse=True)
 
print(employees)
 
# Output:
# [
#   {
#     "name": "Mary Doe",
#     "salary": 70000
#   },
#   {
#     "name": "John Doe",
#     "salary": 60000
#   },
#   {
#     "name": "Jane Doe",
#     "salary": 50000
#   }
# ]