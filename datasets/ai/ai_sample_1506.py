def convert_list_to_2d_array(l):
    # calculate the size of the 2d array
    n = int(len(l) ** 0.5) 
    # create the 2d array
    matrix = [[None for i in range(n)] for j in range(n)] 

    # populate the 2d array
    count = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = l[count]
            count += 1 
    return matrix

print(convert_list_to_2d_array(["a", "b", "c", "d", "e"]))