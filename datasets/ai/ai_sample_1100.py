import random

def generate_grid():
    # create an empty 3x3 grid
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # generate 9 random numbers between 1 and 10
    for i in range(3):
        for j in range(3):
            grid[i][j] = random.randint(1, 10)

    return grid

result = generate_grid()
print(result)