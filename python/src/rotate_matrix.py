def rotateMatrix(matrix):
    X = len(matrix)
    Y = len(matrix[-1])
    M = [[None]*X for _ in range(Y)]
    
    for i in range(Y-1, -1, -1):
        for j in range(X-1, -1, -1):
            M[Y-i-1][X-j-1] = matrix[j][i]
    return M

for m in rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]):
    print(m)

def rotateMatrixInplace(matrix):
    X = len(matrix)
    Y = len(matrix[-1])

    for i in range(Y-1,-1,-1):
        for j in range(X-1,-1,-1):
            matrix[i].append(matrix[j].pop(i))


print("in place")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for m in matrix:
    print(m)

rotateMatrixInplace(matrix)
print("after")
for m in matrix:
    print(m)
rotateMatrixInplace(matrix)
print("after")
for m in matrix:
    print(m)
rotateMatrixInplace(matrix)
print("after")
for m in matrix:
    print(m)
rotateMatrixInplace(matrix)
print("after")
for m in matrix:
    print(m)
