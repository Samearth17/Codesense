# Node class 
class Node: 
 
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 

# Linked list class 
class LinkedList: 
 
    # Function to initialize the Linked List object 
    def __init__(self):  
        self.head = None
 
    # This function returns true if a value x is present in linked list 
    def search(self, x):     
        temp = self.head 
        while temp.next != None: 
            if temp.data == x: 
                return True  # data found 
            temp = temp.next
 
        if temp.data == x: 
            return True # data found 
        return False # data not found 

# Code execution
if __name__=='__main__': 
 
    # Start with the empty list 
    llist = LinkedList() 
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 

# Link first node with second 
    llist.head.next = second  
     
# Link second node with third  
    second.next = third 

# Search value 3 
    if llist.search(3): 
        print("Value found")
    else:
        print("Value not found")