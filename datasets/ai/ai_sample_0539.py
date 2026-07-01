"""
Remove duplicates from an array
"""

def remove_duplicates(arr):
    # Create a set 
    seen = set()
    
    # Traverse the array
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            
    return seen

if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 5, 6]
    print(remove_duplicates(arr))