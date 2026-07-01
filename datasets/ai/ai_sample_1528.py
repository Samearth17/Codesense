from sklearn import tree

# Prepare Input
Input = [['M', 24, 33800, 'Petrol'], 
         ['F', 35, 35000, 'Electric'], 
         ['F', 40, 45000 , 'Petrol'], 
         ['M', 20, 25000, 'Electric'],
         ['M', 30, 32000, 'Petrol'],
         ['F', 50, 60000, 'Electric']]

# Prepare Target
Target = [1, 0, 1, 0, 0, 1]

# Create a decision tree
model = tree.DecisionTreeClassifier()

# Train the model 
model.fit(Input,Target)

# Visualize the decision tree
tree.plot_tree(model)