# Node class  
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 

# Linked List class 
class LinkedList: 
  
    # Function to initialize the Linked List object 
    def __init__(self):   
        self.head = None

# A helper function to check if a given linked list is a palindrome  
def checkPalindrome(root): 
    #base case
    if root == None:
        return True
        
    # Find length of list
    lenList = 0
    iterator = root
    while iterator != None:
        lenList = lenList+1
        iterator = iterator.next
    
    # Find middle pointer
    # If length is even, moving the second pointer right 
    # So, we can get two middle pointers 
    midPtr = root
    for i in range(int(lenList/2)-1):
        midPtr = midPtr.next
    
    # Now pointer is at the exact middle 
    # Checking each next node if its same
    currentNode = midPtr
    prevNode = None
    while currentNode != None:
        nextn = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextn
    
    # now both the halves are swapped 
    # checking each node one by one
    startPtr1 = root
    startPtr2 = prevNode
    
    # if length is odd
    # move the second pointer one step right 
    if lenList%2!=0:
        startPtr2 = startPtr2.next
        
    palindrome = True
    while startPtr1 != None:
        if startPtr1.data != startPtr2.data:
            palindrome = False
            break
            
        startPtr1 = startPtr1.next
        startPtr2 = startPtr2.next
    
    # Re-linking both the pointers 
    currentNode = prevNode
    prevNode = None
    while currentNode != None:
        nextn = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextn
        
    return palindrome

# Driver Code 

# Create a linked list with  
# 1->2->3->2->1 
head = Node(1) 
firstNode = Node(2) 
secondNode = Node(3) 
thirdNode = Node(2) 
fourthNode = Node(1) 
  
# Now link the next pointers 
head.next = firstNode 
firstNode.next = secondNode 
secondNode.next = thirdNode 
thirdNode.next = fourthNode 
  
if(checkPalindrome(head)): 
    print ("Linked List is palindrome")
else: 
    print ("Linked List is not palindrome")