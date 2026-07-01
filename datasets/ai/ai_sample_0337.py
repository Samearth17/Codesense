def calculate_combinations(range):
    count = 0

    # base case
    if len(range) == 0:
        return 0
    if len(range) == 1:
        return 1

    # recursive case
    for i in range:
        sub_set = range[:]
        sub_set.remove(i)
        count += calculate_combinations(sub_set) + 1

    return count

range = [1, 2, 3]
print(calculate_combinations(range))
# Output: 6