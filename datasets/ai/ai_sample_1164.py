def find_palindromes(s):
    n = len(s)
    is_palindrome = [[False for _ in range(n)] for _ in range(n)]
 
    # Palindrome of length 1
    for i in range(n):
        is_palindrome[i][i] = True
    # Palindrome of length 2
    for i in range(n - 1):
        is_palindrome[i][i + 1] = (s[i] == s[i + 1])
    # Palindrome of length >= 3
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
    res = []
    for i in range(n):
        for j in range(i, n):
            if is_palindrome[i][j] and j - i + 1 >= 3:
                res.append(s[i:j + 1])
    return res