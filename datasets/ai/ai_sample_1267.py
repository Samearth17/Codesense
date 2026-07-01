def find_most_frequent(numbers):
    frequency_dict = {}
    for n in numbers:
        if n in frequency_dict:
            frequency_dict[n] += 1
        else:
            frequency_dict[n] = 1
            
    max_frequency = 0
    most_frequent = 0
    for k, v in frequency_dict.items():
        if v > max_frequency:
            max_frequency = v
            most_frequent = k
            
    return most_frequent
    
# Usage
numbers = [1, 2, 3, 1, 2, 2]
most_frequent = find_most_frequent(numbers)
print(most_frequent) # Outputs 2