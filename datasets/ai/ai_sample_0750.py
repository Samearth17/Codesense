# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next
  
    # Function to delete node at position 'index'
    def delete_node(self, index):
  
        # Initialize temp and prev
        temp = self.head 
        prev = None
  
        # Check if index is valid
        if temp is None or index < 0: 
            return
  
        # If index is 0, delete the first node
        if index == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find the node before the node to be deleted
        for i in range(index): 
            prev = temp 
            temp = temp.next
  
        # Unlink the node from linked list 
        prev.next = temp.next
        temp = None
  
  
# Driver Program 
llist = LinkedList()
  
# Create the list 1->2->3->4
llist.head = Node(1) 
second = Node(2) 
third = Node(3) 
fourth = Node(4) 

llist.head.next = second;  # Link first node with second 
second.next = third;  # Link second node with the third node 
third.next = fourth;  # Link third node with the fourth node 

# Delete the node at positions 2
llist.delete_node(2)