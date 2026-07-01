input_list = [1,2,3]

num_elements = len(input_list)

def create_symmetric_matrix(input_list):
    matrix = [[0 for x in range(num_elements)] for y in range(num_elements)]
    
    for i in range(num_elements):
        for j in range(num_elements):
            if i == j:
                matrix[i][j] = input_list[i]
            else:
                matrix[i][j] = input_list[j]
                
    return matrix

res = create_symmetric_matrix(input_list)
print(res)