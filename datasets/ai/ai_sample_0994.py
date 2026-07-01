# Function to sort dictionary by value
def sort_dict(d): 
    # Create a list of tuples
    # sorted by index 1 i.e. value field 
    l = [(k, d[k]) for k in sorted(d, key = d.get, reverse = True)] 
      
    # Create a dictionary from the list  
    # of tuples for sorted value 
    od = OrderedDict(l) 
  
    return od 

# Sample Dictionary
d = {'name':'John', 'age':26, 'salary':3000}

# Calling sort_dict function
print(sort_dict(d))