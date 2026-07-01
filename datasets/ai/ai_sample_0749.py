import itertools

def generate_names(first_names, last_names):
  names = []
  
  for first, last in itertools.product(first_names, last_names):
    names.append(first + ' ' + last)
  
  return names

first_names = ['John', 'Emma', 'Sarah', 'Liam']
last_names = ['Smith', 'Jones', 'Brown', 'Robinson']

names = generate_names(first_names, last_names)
print(names)