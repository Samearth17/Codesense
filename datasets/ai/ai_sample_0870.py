class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isPalindrome(self):
        # your code here
        slow_ptr = self.head
        fast_ptr = self.head
        rev_head = None
        
        while(fast_ptr):
            fast_ptr = fast_ptr.next
            if fast_ptr:
                fast_ptr = fast_ptr.next
                prev = slow_ptr
                slow_ptr = slow_ptr.next
            
            prev.next = rev_head
            rev_head = prev
        
        fast_ptr = self.head
        while(rev_head):
            if fast_ptr.data != rev_head.data:
                return False
            fast_ptr = fast_ptr.next
            rev_head = rev_head.next
        
        return True
    
    def removeDuplicates(self):
        # your code here
        cur_node = self.head
        while cur_node:
            prev_node = cur_node
            next_node = cur_node.next
            while next_node:
                if next_node.data == cur_node.data:
                    prev_node.next = next_node.next
                else:
                    prev_node = next_node
                next_node = next_node.next
            cur_node = cur_node.next