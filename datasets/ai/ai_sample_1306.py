import numpy as np

# Define the automata
cell_size = 10
auto = np.zeros(cell_size)

# Create the display
def display_automata(cells):
 for cell in cells:
 if cell == 0:
 print('█', end="")
 else:
 print(' ', end='')
 print()

# Iterate the automata
for i in range(100):
 temp_auto = np.copy(auto)
 for j in range(cell_size):
 if j == 0:
 value = temp_auto[-1] ^ temp_auto[j] ^ temp_auto[j + 1]
 elif j == cell_size - 1:
 value = temp_auto[j-1] ^ temp_auto[j] ^ temp_auto[0]
 else:
 value = temp_auto[j - 1] ^ temp_auto[j] ^ temp_auto[j + 1]
 auto[j] = value
 display_automata(auto)