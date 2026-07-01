def move_zeroes(lst):
    # Count the number of non-zero elements
    num_non_zeroes = 0
    for num in lst:
        if num != 0:
            num_non_zeroes += 1
  
    # Initialize the new list
    new_lst = []
  
    # Move all non-zeroes to the beginning of the new list
    for i in range(num_non_zeroes):
        new_lst.append(lst[i])
  
    # Append 0's to the end
    for _ in range(len(lst)-num_non_zeroes):
        new_lst.append(0)
  
    # Return the new list
    return new_lst

lst = [3, 0, 1, 0, 5, 0, 2]
result = move_zeroes(lst)
print(result)