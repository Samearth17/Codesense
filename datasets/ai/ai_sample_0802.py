def print_spiral_matrix(n):
    matrix = [[0] * n for i in range(n)]
 
    i = 0
    j = 0
 
    top = 0
    left = 0
    right = n - 1
    bottom = n - 1
 
    direction = 0
 
    while top <= bottom and left <= right:
        if direction == 0:
            for j in range(left, right + 1):
                matrix[top][j] = i
                i += 1
            top += 1
            direction = 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                matrix[i][right] = i
                i += 1
            right -= 1
            direction = 2
        elif direction == 2:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = i
                i += 1
            bottom -= 1
            direction = 3
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = i
                i += 1
            left += 1
            direction = 0
 
    for i in range(n):
        print(matrix[i])