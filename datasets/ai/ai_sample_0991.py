# Bubble sort function in Python
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare the adjacent elements
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input list
arr = [3, 5, 4, 1, 6]

# Function call
bubble_sort(arr)

# Print the sorted array
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
# Output: 1 3 4 5 6