def walk_path(m):
    memo = {}
    def walk(row, col):
        if row == col == len(m) - 1: 
            count = 1
        else:
            if f'{row}{col}' in memo:
                count = memo[f'{row}{col}']
            else:
                count = 0
                if row + 1 < len(m):
                    count += walk(row + 1, col)
                if col + 1 < len(m[row]):
                    count += walk(row, col + 1)
                memo[f'{row}{col}'] = count
        return count
        
    return walk(0,0)

m = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

print(walk_path(m))

m = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
    ]

print(walk_path(m))
