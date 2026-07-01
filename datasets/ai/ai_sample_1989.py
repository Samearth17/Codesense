def spiral_matrix(num_rows, num_columns):
    matrix = [[0] * num_columns for row in range(num_rows)]

    stride = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = 0
    x, y = 0, 0
    val = 1
    while 0 <= x < num_rows and 0 <= y < num_columns:
        matrix[x][y] = val
        x += stride[direction][0]
        y += stride[direction][1]
        if x < 0 or y < 0 or x == num_rows or y == num_columns or matrix[x][y] != 0:
            x -= stride[direction][0]
            y -= stride[direction][1]
            direction += 1
            if direction == len(stride):
                direction = 0
            x += stride[direction][0]
            y += stride[direction][1]
        val += 1
    return matrix