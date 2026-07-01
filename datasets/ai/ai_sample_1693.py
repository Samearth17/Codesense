"""
Extract the first name and the last name from a given full name
"""

def extract_names(full_name):
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    
    return first_name, last_name

if __name__ == '__main__':
    full_name = 'John Smith'
    first_name, last_name = extract_names(full_name)
    print(f'The first name is {first_name} and the last name is {last_name}.')