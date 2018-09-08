'''
    recursive approach
'''
def num_islands(m):
    count, memo = 0, set()
    
    def traverse(row, col):
        key = f'{row},{col}'
        if key not in memo:
            memo.add(key)
            for i in [-1,1]:
                if 0 <= row+i < len(m) and m[row+i][col] == 1:
                    traverse(row+i, col)
                if 0 <= col+i < len(m[row]) and m[row][col+i] == 1:
                    traverse(row, col+i)
            return 1
        else: return 0

    if m:
        for i in range(0, len(m)):
            for j in range(0, len(m[i])):
                if m[i][j] == 1:
                    count += traverse(i, j)

    return count


'''
    iterative approach
'''
def num_islands2(m):
    count, memo = 0, set()

    def bfs(i,j):
        q = [(i,j)]
        while(len(q)):
            i, j = q[0]
            q, key = q[1:], f'{i},{j}'
            if key not in memo:
                memo.add(key)
                for k in [-1,1]:
                    if 0 <= i+k < len(m) and m[i+k][j] == 1:
                        q.append((i+k,j))
                    if 0 <= j+k < len(m[i]) and m[i][j+k] == 1:
                        q.append((i,j+k))
        return 1

    if m:
        for i in range(0,len(m)):
            for j in range(0, len(m[i])):
                if m[i][j] == 1 and f'{i},{j}' not in memo:
                    count += bfs(i,j)
    return count


m = [
        [1,1,0,1],
        [1,1,1,1]
    ]

print(num_islands(m))
print(num_islands2(m))
