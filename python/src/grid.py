from copy import deepcopy

def navigate_grid(g):
    N, output = len(g), []
    def navigate(g, row=0, col=0):
        g[row][col] = 1
        if g[N-1][N-1] == 0:
            if row < N-1: navigate(deepcopy(g), row+1, col)
            if col < N-1: navigate(deepcopy(g), row, col+1)
        else:
            output.append(g)
    navigate(deepcopy(g))
    return l

print(navigate_grid([[0,0,0],[0,0,0],[0,0,0]]))
