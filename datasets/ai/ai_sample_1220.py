# Calculate the Levenshtein Distance between two strings
def levenshteinDistance(str1, str2):
    # Make sure they are the same length
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    # Initialize an empty matrix
    matrix = [[0] * (len(str2) + 1)] * (len(str1) + 1)

    # Fill in the first row and column
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Calculate the rest of the matrix 
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, 
                         matrix[i - 1][j - 1] + cost)

    # Return the resultant matrix
    return matrix[-1][-1]