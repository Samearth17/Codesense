def find_duplicates(list):
    """Identify all the duplicate elements in the given list."""
    seen = set()
    duplicates = set()
    for i in list:
        if i not in seen:
            seen.add(i)
        else:
            duplicates.add(i)
    return list(duplicates)

# Usage Example
list = [1, 2, 3, 2, 1]
duplicates = find_duplicates(list)
print(duplicates)  # [1, 2]