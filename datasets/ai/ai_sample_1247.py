class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_node(head, new_data):
    new_node = Node(new_data)
    if head is None:
        head = new_node
    else:
        last = head
        while(last.next):
            last = last.next
        last.next = new_node
    return head