"""
Create a python script to search a given source code 
for the given keywords and display the search results.
"""
import re

def search_source_code(source_code, keywords):
    matches = []
    for keyword in keywords:
        matches += re.findall(keyword, source_code)
    return matches

if __name__ == '__main__':
    source_code = '''
    #def hou(a, b):
        # some code
    #def calc(a, b):
        # some code
    '''
    keywords = ['hou', 'calc']
    print(search_source_code(source_code, keywords))