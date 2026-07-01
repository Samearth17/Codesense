# Define the array
array = ['school', 'hospital', 'bookstore', 'mall', 'theatre']

# Function to perform linear search
def linearSearch(search_item):
    # Loop through array
    for i in range(len(array)):
        # If search item is found, return its position
        if array[i] == search_item:
            return i
    # If item is not found, return -1
    return -1

# Input search item
s = input("Enter the item to be searched: ")

# Search the item
result = linearSearch(s)

# Print result
if result == -1:
    print("Item not found.")
else:
    print("Item is found at position "+str(result))