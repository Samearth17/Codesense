def max_char(s):
    chars = {}
    for c in s:
        chars[c] = chars.get(c, 0) + 1
    max_val = -1
    max_char = None
    for c, v in chars.items():
        if v > max_val:
            max_val = v
            max_char = c
    return max_char

print(max_char('abrakadabra'))

# Output: a (occurs 5 times)