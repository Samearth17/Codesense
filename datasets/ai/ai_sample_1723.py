# Sort the dataset according to age
sorted_dataset = sorted(dataset, key=lambda x: x['age'])

# Output the sorted dataset
for record in sorted_dataset:
 print(record)

# Output:
{'name': 'Benjamin', 'age': 17}
{'name': 'Adam', 'age': 20}
{'name': 'Olivia', 'age': 20}
{'name': 'Sophia', 'age': 19}
{'name': 'Adam', 'age': 23}
{'name': 'Noah', 'age': 22}
{'name': 'Ethan', 'age': 24}
{'name': 'Mia', 'age': 25}
{'name': 'Ava', 'age': 26}
{'name': 'Isabella', 'age': 27}
{'name': 'John', 'age': 30}
{'name': 'Jasper', 'age': 30}
{'name': 'Daniel', 'age': 33}
{'name': 'Liam', 'age': 35}
{'name': 'Emma', 'age': 35}
{'name': 'Charlotte', 'age': 38}
{'name': 'Eva', 'age': 45}
{'name': 'Amelia', 'age': 44}
{'name': 'Eric', 'age': 40}
{'name': 'Levi', 'age': 40}