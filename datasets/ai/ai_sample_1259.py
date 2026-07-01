"""
Implement a function in Python to convert a pascal triangle to a 2D list
"""
def pascal_to_list(pascal):
    lines = pascal.split('\n')
    # convert list of strings to list of lists
    table = [[int(i) for i in line.split()] for line in lines]
    return table

if __name__ == "__main__":
    pascal = """
    1 
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """
    print(pascal_to_list(pascal))