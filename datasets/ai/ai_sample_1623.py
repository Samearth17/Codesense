def add_two_arrays(arr1, arr2):
    # Padd the smaller array with zeros
    if len(arr1) < len(arr2):
        for _ in range(len(arr2) - len(arr1)):
            arr1.insert(0, 0)
    else:
        for _ in range(len(arr1) - len(arr2)):
            arr2.insert(0, 0)
    
    # Create result array
    res = []

    # Loop through the two arrays
    carry = 0
    for i in range(len(arr1)):
        num = arr1[i] + arr2[i] + carry

        # Check if number is > 10
        if num > 9:
            carry = 1
            num = num%10
        else:
            carry = 0

        res.append(num)

    if carry:
        res.append(1)

    return res

res = add_two_arrays(arr1, arr2)
print(res)