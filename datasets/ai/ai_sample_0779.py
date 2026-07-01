import threading
import numpy as np

mat_1 = np.array([[2, 3, 4], [5, 6, 7]])
mat_2 = np.array([[3, 4, 5], [6, 7, 8]])

def matrix_sum(a, b):
    return a + b

threads = []
for i in range(len(mat_1)):
    thread = threading.Thread(target=matrix_sum, args=(mat_1[i], mat_2[i]))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(matrix_sum(mat_1, mat_2))