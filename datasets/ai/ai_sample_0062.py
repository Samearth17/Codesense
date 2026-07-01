def removeItem(list, item):
    # loop through the list
    for i in list:
        # check if the element is the item to remove
        if i == item:
            # remove the item
            list.remove(i)
    # return the list
    return list

#example
list = [1, 2, 3, 4, 2, 5, 2]
result = removeItem(list, 2)

print(result)
# Output: [1, 3, 4, 5]