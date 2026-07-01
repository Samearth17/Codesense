import ast
import logging

from pygount import SourceAnalysis

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Input code
code = """
def find_bugs(code):
    
    analyzed_code = SourceAnalysis.from_string(language='python', text=code)
    bugs = []

    for function in code: 
        if 'fopen' in function.body:
            bugs.append('Got a potential vulnerability!')

    return bugs
"""

# Parsed syntax tree
tree = ast.parse(code)

# Find all functions
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        # Get the code for the function
        function_code = ast.get_source_segment(code, node)
        bugs = find_bugs(function_code)
        for bug in bugs:
            logging.warning(bug)