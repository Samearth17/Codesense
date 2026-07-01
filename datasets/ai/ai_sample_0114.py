def calculate_result(obj_list):
 result_list = []

 for obj in obj_list:
  result = {}
  result['id'] = obj['id']
  result['result'] = sum(obj['inputs'])

 result_list.append(result)

return result_list

obj_list = [{"id": 1, "inputs": [1,2,3]}, 
{"id": 2, "inputs": [2,3,4]}]

print(calculate_result(obj_list))

# Output: [{'id': 1, 'result': 6}, {'id': 2, 'result': 9}]