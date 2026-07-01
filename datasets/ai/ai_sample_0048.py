import collections

class Maze:
    def __init__(self, n, m):
        self._n, self._m = n, m
        self._grid = [[None] * m for _ in range(n)]

    def solve_maze(self):
        result, found = [], False
        start, end = (0, 0), (self._n-1, self._m-1)

        for i in range(self._n):
            for j in range(self._m):
                if self._grid[i][j] == 1:
                    value = 0
                    self._find_omega(i, j, value, result, start, end,
                                     found)
                    return result

    def _find_omega(self, i, j, value,
                    result, start, end, found):
        rowNbr, colNbr = [-1, 0, 0, 1], [0, -1, 1, 0]

        if (i, j) == end:
            found = True
            result.append(value)
            return

        if found == True:
            return

        self._grid[i][j] = 0
        for k in range(4):
            if self._on_board(i + rowNbr[k], j + colNbr[k]):
                self._find_omega(i + rowNbr[k], j + colNbr[k],
                                 value + 1, result,
                                 start, end, found)

    def _on_board(self, i, j):
        return 0 <= i < self._n and 0 <= j < self._m and self._grid[i][j] == 1