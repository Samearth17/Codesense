def shortest_path(matrix, start, end):
  queue = []
  min_len = math.inf
  queue.append([start])
  while queue:
    path = queue.pop(0)
    x, y = path[-1]
    if (x, y) == end:
      if len(path) < min_len:
        min_len = len(path)
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      new_x, new_y = x + dx, y + dy
      if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
        if matrix[new_x][new_y] == 0:
          queue.append(path + [(new_x, new_y)])
  return min_len