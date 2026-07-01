def longest_substring(string, k):
    start, distinct, max_length = 0, 0, 0
    frequency = {}
    for end in range(len(string)):
        frequency[string[end]] = frequency.get(string[end], 0) + 1
        if frequency[string[end]] == 1:
            distinct += 1
 
        while distinct > k:
            frequency[string[start]] -= 1
            if frequency[string[start]] == 0:
                distinct -= 1
            start += 1
 
        max_length = max(max_length, end - start + 1)
    return max_length

print(longest_substring(string, k))