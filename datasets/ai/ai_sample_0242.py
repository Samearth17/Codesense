def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        dict_str1 = {}
        dict_str2 = {}
        for i in range(len(str1)):
            if str1[i] not in dict_str1:
                dict_str1[str1[i]] = 1
            else:
                dict_str1[str1[i]] += 1
            if str2[i] not in dict_str2:
                dict_str2[str2[i]] = 1
            else:
                dict_str2[str2[i]] += 1
        return dict_str1 == dict_str2

print(is_permutation(str1, str2))