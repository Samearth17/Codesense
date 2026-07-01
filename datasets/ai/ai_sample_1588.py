class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def detect_loop(head):
  fast_ptr = head
  slow_ptr = head

  while (slow_ptr and fast_ptr and fast_ptr.next):
      slow_ptr = slow_ptr.next
      fast_ptr = fast_ptr.next.next
      if slow_ptr == fast_ptr:
          return slow_ptr

  return None

def remove_loop(head, loop_ptr):
  slow_ptr = head
  fast_ptr = loop_ptr

  while (slow_ptr != fast_ptr):
      slow_ptr = slow_ptr.next
      fast_ptr = fast_ptr.next

  prev_slow_ptr = None
  while (slow_ptr != fast_ptr):
    prev_slow_ptr = slow_ptr
    slow_ptr = slow_ptr.next
    fast_ptr = fast_ptr.next

  prev_slow_ptr.next = None