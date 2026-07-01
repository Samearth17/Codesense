# initialize size
SIZE = 256

# defining Node class
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

# defining HashTable
class HashTable:
    def __init__(self):
        self.table = [None]*SIZE

    # hash function
    def hash_function(self, key):
        return key % SIZE

    # insert data
    def insert(self, key, data):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = Node(key, data)
        else:
            temp_node = self.table[index]

            while temp_node.next:
                temp_node = temp_node.next

            temp_node.next = Node(key, data)

    # search data
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return "No data found!"
        else:
            temp_node = self.table[index]
            while temp_node and temp_node.key != key:
                temp_node = temp_node.next
            if not temp_node:
                return "No data found!"
            else:
                return temp_node.data

    # get size
    def get_size(self):
        count = 0
        for item in self.table:
            if item:
               count += 1
            while item.next:
                count += 1
                item = item.next
        return count