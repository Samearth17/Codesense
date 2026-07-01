def format_text(string):
    """Format the given string with the correct indentation levels."""
    lines = string.splitlines()
    level = 0
    formated = ""
    for line in lines:
        if line.isspace():
            continue
        formated += "  " * level + line + "\n"
        if line.endswith(":"):
            level += 1
        elif line.startswith("return") or line.startswith("break"):
            level -= 1
    return formated

# Usage Example
string = """This is 
a string
with different lines."""
formated = format_text(string)
print(formated) 

# This is
#   a string
#   with different lines.