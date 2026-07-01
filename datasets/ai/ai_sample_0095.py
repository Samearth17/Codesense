def longest_common_substring(str1, str2):
    match = 0
    substr = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            l = 0
            while (i + l < len(str1) and j + l < len(str2) and str1[i + l] == str2[j + l]):
                l += 1
            if l > match:
                substr = str1[i:i + l]
                match = l
    return substr

result = longest_common_substring("Helwallomst", "Welcome")
print(result)