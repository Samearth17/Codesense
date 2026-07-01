def classify(data):
  # Initialize two empty lists
  classA = []
  classB = []
  
  # Iterate over data
  for k,v in data.items():
    # Populate classA and classB
    if v == 1:
      classA.append(k)
    else:
      classB.append(k)
    
  # Return the two classes
  return classA, classB

# Input data  
Data = {"A": 1, "B": 0, "C": 1, "D": 1, "E": 0}

# Call the classify function
classA, classB = classify(Data)

# Print the results
print(classA) # ['A', 'C', 'D']
print(classB) # ['B', 'E']