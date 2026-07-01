class ListUnique:
    
    def __init__(self,list1):
        # set up empty list
        self.list1 = []
        
        # loop through input list
        for x in list1:
            # add element to list if it is not already in the list
            if x not in self.list1:
                self.list1.append(x)
                
    # returns the modified list
    def get_list(self):
        return self.list1

list1 = ['a','b','b','c','a','c']

# create instance of ListUnique
lu = ListUnique(list1)

# print the modified list
print(lu.get_list()) # prints ['a', 'b', 'c']