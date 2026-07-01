def longest_common_substring(s1, s2):
    longest_length = 0
    longest_substring = ""

    for i in range(min(len(s1), len(s2))):
        substr = s1[i]

        for j in range(i + 1, min(len(s1), len(s2))):
            if s2[j] == s1[i]:
                substr += s1[j]

            if len(substr) > longest_length and substr in s2:
                longest_length = len(substr)
                longest_substring = substr

    return longest_substring

result = longest_common_substring('string', 'longest')
print(result)