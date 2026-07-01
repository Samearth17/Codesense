def find_substring(source, substring):
    '''This function returns the start index of a substring in given string '''
    if substring not in source:
        return -1
    i=0
    while i < len(source):
        if source[i] == substring[0]:
            flag = True
            for j in range(len(substring)):
                if substring[j] != source[i+j]:
                    flag = False
                    break
            if flag:
                return i
        i += 1
    return -1