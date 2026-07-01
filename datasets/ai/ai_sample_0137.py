class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self): 
        self.head = None
 
    def append(self, new_data): 
        new_node = Node(new_data) 
        if self.head is None:
            self.head =  new_node
        else: 
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
 
    def prepend(self, new_data):
        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node 
        self.head = new_node

    def reverse(self):
        curr_node = self.head
        while curr_node:
            temp = curr_node.next
            curr_node.next = curr_node.prev
            curr_node.prev = temp
            curr_node = curr_node.prev
        if temp:
            self.head = temp.prev