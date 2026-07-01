def compareLists(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = compareLists(list1, list2)

print(f'Are the elements in the lists the same? {result}')

# Output: Are the elements in the lists the same? False