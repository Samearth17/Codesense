class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = node