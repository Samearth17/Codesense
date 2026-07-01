def find_second_largest_number(input_list):
    '''Finds the second largest number in a given list.'''
    first = float("-infinity")
    second = float("-infinity")

    for num in input_list:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second

list = [2, 10, 7, 5, 8]
print(find_second_largest_number(list))
# Output: 8