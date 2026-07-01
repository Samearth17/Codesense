def findLongestPalindrome(s):
    if s is None or s == '':
        return ''

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandFromMiddle(s, i, i)
        len2 = expandFromMiddle(s, i, i+1)
        len_tot = max(len1, len2)
        if len_tot > end - start:
            start = i - (len_tot-1)//2
            end = i + len_tot//2
    return s[start:end+1]
  
def expandFromMiddle(s, left, right):
    while left > -1 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1