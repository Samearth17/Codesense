def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    mid = len(data)//2
    if len(data) % 2 == 0:
        return (sorted_data[mid] + sorted_data[mid-1])/2
    else:
        return sorted_data[mid]

def mode(data):
    counted_data = dict()
    for item in data:
        if item not in counted_data:
            counted_data[item] = 1
        else:
            counted_data[item] += 1
    highest_count = 0
    modes = []
    for key, value in counted_data.items():
        if value > highest_count:
            modes = [key]
            highest_count = value
        elif value == highest_count:
            modes.append(key)
    if len(modes) == len(data):
        modes = []
    return modes