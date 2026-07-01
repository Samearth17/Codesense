def count_palindrome_substrings(s):
    # Create a boolean matrix to store the values
    matrix = [[False for _ in range(len(s))] for _ in range(len(s))]

    # Initialize the substrings with length 1
    for i in range(len(s)):
        matrix[i][i] = True

    # Initialize the substrings with length 2
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            matrix[i][i+1] = True

    # Iterate through the string and find the substrings
    for substring_length in range(3, len(s) + 1):
        for i in range(0, len(s) - substring_length + 1):
            j = i + substring_length - 1
            if s[i] == s[j] and matrix[i+1][j-1]:
                matrix[i][j] = True

    # Iterate through the matrix and count the palindrome substrings
    count = 0
    for row in matrix:
        for elem in row:
            if elem:
                count += 1

    return count