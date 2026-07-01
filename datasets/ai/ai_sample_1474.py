def merge_sort(arr):
 if len(arr) >1: 
 mid = len(arr)//2  #Finding the mid of the array 
 L = arr[:mid]   # Dividing the array elements  
 R = arr[mid:] # into 2 halves 
  
 merge_sort(L) # Sorting the first half 
 merge_sort(R) # Sorting the second half 
  
 i = j = k = 0
  
 # Copy data to temp arrays L[] and R[] 
 while i < len(L) and j < len(R): 
 if L[i] < R[j]: 
 arr[k] = L[i] 
 i+=1
 else: 
 arr[k] = R[j] 
 j+=1
 k+=1
  
 # Checking if any element was left 
 while i < len(L): 
 arr[k] = L[i] 
 i+=1
 k+=1
  
 while j < len(R): 
 arr[k] = R[j] 
 j+=1
 k+=1
  
def print_list(arr): 
 for i in range(len(arr)):         
 print(arr[i],end=" ") 
 print() 
  
# Driver code to test above 
if __name__ == '__main__': 
 arr = [5,3,6,8,10,1,4,7] 
 print ("Given array is", end="\n")  
 print_list(arr) 
 merge_sort(arr) 
 print("Sorted array is: ", end="\n") 
 print_list(arr)