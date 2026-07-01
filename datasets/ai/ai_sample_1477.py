import ast

def parse_variables(source_code):
    tree = ast.parse(source_code)
    variable_names = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            variable_names.append(node.targets[0].id)

    return variable_names

if __name__ == '__main__':
    source_code = "name = 'Abhishek'\nage = 23\n\ndef printDetails():\n    print('My name is ' + name)\n    print('I am ' + str(age) + ' years old')\n\nprintDetails()"
    variable_names = parse_variables(source_code)
    print(variable_names)