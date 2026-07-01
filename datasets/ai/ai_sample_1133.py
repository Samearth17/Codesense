def compare_objects(obj1, obj2):
    # Compare type
    if type(obj1) != type(obj2):
        return False
    # Compare values
    if isinstance(obj1, (int, float)):
        if obj1 != obj2:
            return False
    elif isinstance(obj1, str):
        if obj1 != obj2:
            return False
    elif isinstance(obj1, tuple):
        if obj1 != obj2:
            return False
    elif isinstance(obj1, list):
        if len(obj1) == len(obj2):
            if all(x == y for x, y in zip(obj1, obj2)):
                return True
            else:
                return False
    elif isinstance(obj1, dict):
        if len(obj1) == len(obj2):
            if obj1 == obj2:
                return True 
            else:
                return False

    return True