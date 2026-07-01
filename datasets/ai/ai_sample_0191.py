def longest_substring(str_1, str_2):
    len_1 = len(str_1)
    len_2 = len(str_2)
    longest_substring = ''
    for x in range(len_1):
        for y in range(len_2):
            if str_1[x] == str_2[y]:
                cur_substring = str_1[x]
                while (x + 1 < len_1 and y + 1 < len_2 and
                       str_1[x + 1] == str_2[y + 1]):
                    cur_substring += str_1[x + 1]
                    x += 1
                    y += 1
                    if len(cur_substring) > len(longest_substring):
                        longest_substring = cur_substring
    return longest_substring

longest_sub = longest_substring(str_1, str_2)
print(longest_sub)