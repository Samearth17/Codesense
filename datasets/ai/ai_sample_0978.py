def get_dict_with_prefix(dict_data, prefix):
  new_dict = {}
  for key, value in dict_data.items():
    if key.startswith(prefix):
      new_dict[key] = value

  return new_dict

dict_data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "prefix_key1": "value4",
    "prefix_key2": "value5"
}
prefix = "prefix_"

new_dict = get_dict_with_prefix(dict_data, prefix)

print(new_dict)  # Output: {'prefix_key1': 'value4', 'prefix_key2': 'value5'}