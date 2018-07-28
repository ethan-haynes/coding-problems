from copy import deepcopy

def grid(g):
    N, l = len(g), []
    def _g(grid, row=0, col=0):
        grid[row][col] = 1
        if grid[N-1][N-1] == 0:
            if col < N-1 and row < N-1:
                _g(deepcopy(grid), row+1, col), _g(deepcopy(grid), row, col+1)
            elif col < N-1:
                _g(deepcopy(grid), row, col+1)
            else:
                _g(deepcopy(grid), row+1, col)
        else:
            l.append(grid)
    _g(deepcopy(g))
    return l

print(grid([[0,0,0],[0,0,0],[0,0,0]]))
