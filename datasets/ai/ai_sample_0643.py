class Node: 
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data,)
            temp = temp.next
 
    # Function to remove a node from linked list
    def remove(self, value): 
        temp = self.head
  
        # If head node itself holds the key 
        # or multiple occurrences of key
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return 
        if temp == self.head: 
            self.head = temp.next 
        else: 
            prev.next = temp.next
 
    # This code is contributed by Sachin Bisht