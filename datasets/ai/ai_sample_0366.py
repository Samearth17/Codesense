# Python 3 program to count the number of occurrences 
# of an element in the given list

# function to count the number of occurrences 
def countOccurrences(nums, query):
    count = 0
    for num in nums:
        if query == num:
            count = count + 1
    return count

# Driver code 
nums = [1, 2, 3, 2, 3, 2, 4]

# Function Call
query = 2
print("{0} occurs {1} times".format(query, countOccurrences(nums, query)))