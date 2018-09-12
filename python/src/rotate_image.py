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

def rotate_image2(m):
    if m:
        for i in range(len(m) - 1, -1, -1):
            for j in range(len(m))):
                n = m[i].pop(0)
                m[j].append(n)

def rotate_image_uneven(m):
    if m:
        row, col = len(m), len(m[0])
        for i in range(row - 1, -1, -1):
            for j in range(col):
                n = m[i].pop(0)
                if len(m) <= j:
                    m.append([])
                m[j].append(n)
                if len(m[i]) == 0:
                    m.pop()

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
