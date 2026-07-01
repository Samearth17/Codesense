def get_all_keys(input_dict):
    keys = set()
    if isinstance(input_dict, dict):
        keys.update(input_dict.keys())
        for v in input_dict.values():
            keys.update(get_all_keys(v))
    return keys

dict1 = {
    "key1": [1,2],
    "key2": [2,3],
    "key3": {
        "key4": [3,4]
    }
}

unique_items = get_all_keys(dict1)
print(unique_items)