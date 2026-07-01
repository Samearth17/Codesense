def print_pattern(data):
    words = data.split(" ")
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    for i in range(max_length):
        line = ""
        for word in words:
            if i < len(word):
                line += word[i] + "  "
            else:
                line += "   " 
        print(line)

result = print_pattern("D O G S U")