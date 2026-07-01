# Python program to delete a node from Linked List  
  
# Node class  
class Node:  
  
    # Function to initialize the node object  
    def __init__(self, data):  
        self.data = data  # Assign data  
        self.next = None  # Initialize next as null  
  
  
# Linked List class contains a Node object  
class LinkedList:  
  
    # Function to initialize head  
    def __init__(self):  
        self.head = None
  
    # Function to delete a node  
    def deleteNode(self, node): 
  
        # Store head node  
        temp = self.head  
  
        # If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp == node):  
                self.head = temp.next
                temp = None
                return
  
        # Search for the key to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while(temp is not None):  
            if temp == node:  
                break
            prev = temp  
            temp = temp.next 
  
        # if key is not present in linked list  
        if(temp == None):  
            return
  
        # Unlink the node from linked list  
        prev.next = temp.next
  
        temp = None