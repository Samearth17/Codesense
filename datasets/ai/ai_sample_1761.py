def find_permutations(s):
    # If a string is empty, return an empty list
    if len(s) == 0:
        return [s]

    # Take the first character as the prefix
    prefix = s[0]
    # Take the rest of the string as the suffix
    suffix = s[1:]

    # Find all the possible permutations of the suffix
    permutations = find_permutations(suffix)

    result = []
    # Insert the prefix into all possible positions in each permutation
    for permutation in permutations:
        for i in range(len(permutation)+1):
            result.append(permutation[:i] + prefix + permutation[i:])
    return result