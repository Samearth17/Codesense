def optimize_code(code):
    optimized_code = ""
    lines = code.splitlines()
    indentation_level = 0

    for line in lines:
        # Remove redundant white space and apply proper indentation
        optimized_code += " " * indentation_level + line.strip() + "\n"

        # Increment/Decrement indentation level 
        if line.endswith(":"):
            indentation_level += 4
        else:
            if line[0] not in ["#", ""]:
                indentation_level -= 4
        indentation_level = max(indentation_level, 0) # prevent it going below 0

    return optimized_code