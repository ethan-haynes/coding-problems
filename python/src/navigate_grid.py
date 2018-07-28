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
    return output

def navigate_grid_with_obstacles(g):
    N, output, block = len(g), [], 'x'
    if g[N-1][N-1] == block: return []
    def navigate(g, row=0, col=0):
        g[row][col] = 1
        if g[N-1][N-1] == 0:
            if row < N-1 and g[row+1][col] != block:
                navigate(deepcopy(g), row+1, col)
            if col < N-1 and g[row][col+1] != block:
                navigate(deepcopy(g), row, col+1)
        else:
            output.append(g)
    navigate(deepcopy(g))
    return output

for grid in navigate_grid([[0,0,0],[0,0,0],[0,0,0]]):
    print("---------------")
    for row in grid:
        print(row)
    print("---------------")

for grid in navigate_grid_with_obstacles([[0,0,0],[0,0,'x'],[0,0,0]]):
    print("---------------")
    for row in grid:
        print(row)
    print("---------------")

for grid in navigate_grid_with_obstacles([[0,0,0],[0,'x',0],[0,0,0]]):
    print("---------------")
    for row in grid:
        print(row)
    print("---------------")

print(navigate_grid_with_obstacles([[0,0,0],[0,0,0],[0,0,'x']]))
