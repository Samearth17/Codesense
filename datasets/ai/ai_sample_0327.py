#Using Python

def max_frequency_element(data):
    # Create an empty dictionary to store the frequency of each element
    frequency = {}
    
    # Iterate over the list and fill in the frequency dictionary
    for x in data:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1
            
    # Now find the key with the maximum frequency
    maximum_frequency = 0
    max_frequency_element = None
    
    for key, value in frequency.items():
        if value > maximum_frequency:
            maximum_frequency = value
            max_frequency_element = key
            
    return max_frequency_element

data = [1, 4, 2, 6, 2, 1, 2, 9]
max_frequency_element = max_frequency_element(data)
print(max_frequency_element)
# Output: 2