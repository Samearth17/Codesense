def parseStringToDict(string): 
    # Split string into key-value pairs
    pairs = string.split(',')
    
    # Create an empty dict for storing the key-value pairs
    values = {} 
    
    # Iterate over the key-value pairs
    for pair in pairs: 
        key, value = pair.split('=')
        values[key] = value
    
    # Return the dictionary
    return values

# Example usage
mapping = parseStringToDict(string)
# Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}