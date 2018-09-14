def min_path_sum(grid):
    memo = {}
    def minP(i, j):
        key = f'{i},{j}'
        if key not in memo:
            if i == len(grid) - 1 and j == len(grid[i]) - 1:
                memo[key] = grid[i][j]
            else:
                memo[key] = grid[i][j] + min(
                    minP(i+1, j) if i+1 < len(grid) else float('inf'),
                    minP(i, j+1) if j+1 < len(grid[i]) else float('inf')
                )
        return memo[key]
    return minP(0,0)

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(min_path_sum(grid))
