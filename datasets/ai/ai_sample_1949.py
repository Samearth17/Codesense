def search(tree, searchTerm):
 if tree['value'] == searchTerm:
 return True
 
 if tree['left'] != None:
 if search(tree['left'], searchTerm):
 return True
 
 if tree['right'] != None:
 if search(tree['right'], searchTerm):
 return True
 
 return False

tree = {value: 24, left: {value: 19, left: {value: 12, left: None, right: None}, right: None}, right: {value: 38, left: None, right: None}}
search_term = 12

if search(tree, search_term):
 print("Value found")
else:
 print("Value not found")