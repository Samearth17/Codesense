class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def reverseList(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
  
    def compareLists(self, head1, head2): 
        while(head1 and head2): 
            if head1.data != head2.data: 
                return 0
            head1 = head1.next
            head2 = head2.next
        if (head1 and not head2) or (head2 and not head1): 
            return 0
        return 1
  
    def checkPalindrome(self): 
        slow_ptr = self.head 
        fast_ptr = self.head 
        count = 0
        while(fast_ptr is not None and fast_ptr.next is not None): 
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            count+=1
        second_half = self.reverseList() 
        isPalindrome = self.compareLists(self.head, second_half) 
        
        self.reverseList() 
        if isPalindrome: 
            return True
        else: 
            return False
  
llist = LinkedList() 
llist.push(3)
llist.push(5)
llist.push(6)
llist.push(6)
llist.push(5)
llist.push(3)
llist.checkPalindrome()  # Output: True