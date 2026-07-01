class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, x):
        low = 0
        high = len(self.arr) - 1
        while low <= high: 
            mid = (high + low) // 2   
  
            # Check if x is present at mid 
            if self.arr[mid] < x: 
                low = mid + 1
  
            # If x is greater, ignore left half 
            elif self.arr[mid] > x: 
                high = mid - 1
  
            # If x is smaller, ignore right half 
            else: 
                return mid 
  
        # If we reach here, then the element was not present 
        return -1