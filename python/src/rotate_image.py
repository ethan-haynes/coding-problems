"""
    m=matrix
    Runtime beats 100.00 % of python3 submissions on leetcode.
"""
def rotate_image(m=[]):
    length = len(m)
    if length == 0: return m

    for i in range(length):
        row = length-i-1
        for j in range(length):
            m[j] += [m[row][j]]
        m[row] = m[row][length:]
    return m

print(rotate_image([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))

print(rotate_image([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]))
