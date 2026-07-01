class SinglyLinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


def delete_node(node):
    node.value = node.next_node.value
    node.next_node = node.next_node.next_node

if __name__ == '__main__':
    a = Node(2)
    b = Node(3)
    a.set_next_node(b)
    delete_node(a)
    print(b.get_value())