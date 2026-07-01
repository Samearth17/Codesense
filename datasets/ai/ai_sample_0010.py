def longest_common_subsequence(string1, string2):
    table = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]

    for i, x in enumerate(string1):
        for j, y in enumerate(string2):
            if x == y:
                table[i+1][j+1] = table[i][j]+1
            else:
                table[i+1][j+1] = max(table[i+1][j], table[i][j+1])

    result = ""
    x, y = len(string1), len(string2)
    while x != 0 and y != 0:
        if table[x][y] == table[x-1][y]:
            x -= 1
        elif table[x][y] == table[x][y-1]:
            y -= 1
        else:
            result = string1[x-1] + result
            x -= 1
            y -= 1
    return result

result = longest_common_subsequence("ABCDF", "ABECD")
print(result)