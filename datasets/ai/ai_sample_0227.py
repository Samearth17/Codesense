"""
Write a Python program to create a class for managing a linked list.
"""

# Create the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Create the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addNode(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
            
    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next