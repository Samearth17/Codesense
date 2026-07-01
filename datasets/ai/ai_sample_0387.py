def generate_matrix(m, n):
    matrix = ""
    # generate the matrix row by row
    for i in range(m):
        row = ""
        # generate a single row with n columns
        for j in range(n):
            row += str(random.randint(-100, 100)) + " "
        matrix += row + "\n"
    return matrix

matrix = generate_matrix(3, 5)
print(matrix)
# 23 12 -72 -35 47
# -6 67 42 -54 95
# 93 13 75 -9 -63