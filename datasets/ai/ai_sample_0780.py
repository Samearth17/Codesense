import copy

def find_zero(state):
    for i in range(9):
        if state[i] == 0:
            return i

def move_up(state):
    new_state = copy.copy(state)
    index = find_zero(state)
    x = index % 3
    y = int(index / 3) 
    if y == 0:
        return None
    temp = state[index - 3]
    new_state[index - 3] = 0
    new_state[index] = temp
    return new_state
    
def move_down(state):
....

def move_left(state):
....

def move_right(state):
....

def bfs(initial_state, goal_state):
....

def main():
   initial_state = [7, 8, 0, 2, 3, 5, 4, 1, 6]
   goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   solution = bfs(initial_state, goal_state)
   print(solution)

main()