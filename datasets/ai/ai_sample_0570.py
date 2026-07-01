# Python program to detect cycle in a graph 
  
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
class LinkedList: 
    def __init__(self):  
        self.head = None
  
    def printList(self): 
        head_node = self.head 
        while head_node != None: 
            print(head_node.data) 
            head_node = head_node.next
  
    # Function to detect and remove loop 
    # in a LinkedList 
    def detectAndRemoveLoop(self): 
        # If list is empty or has only one node 
        # without loop 
        if self.head is None or self.head.next is None: 
            return
  
        slow_ptr = fast_ptr = self.head 
        while (fast_ptr and fast_ptr.next): 
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
  
            if slow_ptr == fast_ptr: 
                self.removeLoop(slow_ptr) 
  
    # Function to remove loop 
    def removeLoop(self, loop_ptr): 
        ptr1 = self.head 
        while (1): 
            ptr2 = loop_ptr
            while (ptr2.next != loop_ptr and ptr2.next != ptr1): 
                ptr2 = ptr2.next
  
            # If ptr2 has found ptr1 then there is a  
            # loop. So break the loop 
            if ptr2.next == ptr1: 
                break 
  
            ptr1 = ptr1.next 
  
        # If a loop is found then set the next  
        # node of ptr2 to None 
        ptr2.next = None 
  
if __name__ == '__main__': 
    # Driver program 
    llist = LinkedList() 
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    llist.head.next = second 
    second.next = third 
  
    # loop 
    llist.head.next.next.next = llist.head 
  
    llist.detectAndRemoveLoop() 
  
    print("Linked List after removing loop") 
    llist.printList()