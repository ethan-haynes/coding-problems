def mm(n, m1, m2, m):
    for i in range(0,n):
        for j in range(0,n):
            val = 0
            for k  in range(0,n):
                val += m1[i][k] * m2[k][j]
            m[i][j] = val
    return m
n=2
print(mm(
    n,
    [[1,3],[4,2]],
    [[1,3],[2,1]],
    [x[:] for x in [[0] * n] * n]
    )
)
