def compareStrings(string1, string2):
    result = 0

    if len(string1) != len (string2):
        result += 1
    else:
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                result += 1
    return result


if __name__ == '__main__':
    string1 = 'python'
    string2 = 'perl'
    print(compareStrings(string1, string2))
    
Output: 3