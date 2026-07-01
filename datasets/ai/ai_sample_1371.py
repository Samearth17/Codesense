# Python program to demonstrate Min Heap 
from heapq import heappop, heappush 
  
class MinHeap: 
   
    def __init__(self): 
        self.heap = list() 
   
    # Inserts a new key 'k'  
    def push(self, k): 
        heappush(self.heap, k)            
  
    # Decrease value of key at index 'i' to new_val 
    # It is assumed that new_val is smaller than heap[i] 
    def decreaseKey(self, i, new_val): 
        self.heap[i] = new_val  
        while(i != 0 and self.heap[int((i - 1) / 2)] > self.heap[i]): 
            //Swapping the two keys 
            self.heap[i] = self.heap[int((i - 1) / 2)] 
            self.heap[int((i - 1) / 2)] = self.heap[i] 
            i = int((i - 1) / 2); 
  
    # Method to remove minium element from min heap 
    def pop(self): 
        if self.heap: 
            # Replace root with last element of the heap
            self.heap[0] = self.heap[len(self.heap) - 1] 
            # Remove last element
            self.heap.pop() 
            # Heapify the root element
            self.minHeapify(0) 
        else: 
            return None
   
    # This function mainly calls minHeapify of the root. 
    def minHeapify(self, i): 
        l = 2 * i + 1     
        r = 2 * i + 2     
        smallest = i 
        if l < len(self.heap) and self.heap[i] > self.heap[l]: 
            smallest = l 
        if r < len(self.heap) and self.heap[smallest] > self.heap[r]: 
            smallest = r 
        if smallest != i: 
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i] 
            self.minHeapify(smallest)