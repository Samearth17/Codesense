def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
##
5. Instruction: Create a Python program to detect a cycle in a linked list.
5. Input:
Not applicable
5. Output:
def detectLoop(head): 
    slowPtr = head 
    fastPtr = head 
  
    while(slowPtr and fastPtr and fastPtr.next): 
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
  
        if slowPtr == fastPtr: 
            return True
  
    return False ## No cycle detected