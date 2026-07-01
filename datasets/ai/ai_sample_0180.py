def find_consecutive_integers(lst, k):
    # Edge cases
    if k > sum(lst) or k < 0:
        return -1
 
    # Create a window and move it's boundaries
    l, h, curr_sum = 0, 0, 0
    while h < len(lst):
        # Sum of current window
        curr_sum += lst[h] 
 
        # See if the window sum equals k
        while curr_sum > k and l <= h:
            curr_sum -= lst[l]
            l += 1
 
        # When window sum is equal to k, print the winow
        if curr_sum == k:
            return lst[l:h+1]
 
        # Move the window one step at a time
        h += 1
 
    # If window size reaches last element and no window is 
    # found
    return -1
 
lst = [1,3,5,7,9]
k = 10
print(find_consecutive_integers(lst, k)) # Output: [3,5,7]