def check_duplicates(arr):
    # Create a set to store elements
    s = set()

    # Iterate through the array and check if element is in set
    for num in arr:
        if num in s:
            return True
        else:
            s.add(num)
    return False

arr = [3, 5, 2, 4, 2]

# Print the result
if check_duplicates(arr):
    print('Array contains duplicates')
else:
    print('Array has no duplicates')

// Output: Array contains duplicates