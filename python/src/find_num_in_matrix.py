import math

the_matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

def find_with_loop(m, n):
    for i in range(0, len(m)):
        for j in range(0,len(m[i])):
            if m[i][j] == n:
                return i,j
    return -1,-1

def find_with_binary_search(m, n):
    def bsY(lowY, highY):
        y = int(math.floor((highY+lowY)/2))
        h = m[y][len(m[y])-1]
        l = m[y][0]

        if l <= n and n <= h:
            return y
        if lowY == highY:
            return -1
        elif n > h:
            return bsY(y+1, highY)
        elif n < l:
            return bsY(lowY, y)

    def bsX(y, lowX, highX):
        x = int(math.floor((highX+lowX)/2))
        if m[y][x] == n:
            return y,x
        if lowX == highX:
            return -1, -1
        elif n > m[y][x]:
            return bsX(y, x+1, highX)
        elif n < m[y][x]:
            return bsX(y, lowX, x)

    y = bsY(0,len(m)-1)
    return bsX(y, 0, len(m[y])-1)

print(find_with_loop(the_matrix, 2))
print(find_with_loop(the_matrix, 4))
print(find_with_loop(the_matrix, 5))
print(find_with_loop(the_matrix, 8))

print('-----------------------------------')
print(find_with_binary_search(the_matrix, 2))
print(find_with_binary_search(the_matrix, 4))
print(find_with_binary_search(the_matrix, 5))
print(find_with_binary_search(the_matrix, 8))
