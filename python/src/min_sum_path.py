def min_sum_path(matrix, row=0, col=0):
    rows = len(matrix)
    cols = len(matrix[rows-1])
    current_node = matrix[row][col]
    paths = []

    if row == rows-1 and col == cols-1:
        return current_node
    if row+1 < rows:
        paths.append(min_sum_path(matrix, row+1, col))
    if col+1 < cols:
        paths.append(min_sum_path(matrix, row, col+1))
    return current_node + min(paths)


def min_sum_path_f(matrix):
    rows = len(matrix)
    cols = len(matrix[rows-1])

    def _msp(row=0, col=0):
        current_node = matrix[row][col]
        paths = []

        if row == rows-1 and col == cols-1:
            return current_node
        if row+1 < rows:
            paths.append(_msp(row+1, col))
        if col+1 < cols:
            paths.append(_msp(row, col+1))
        
        return current_node + min(paths)
    return _msp


matrix = [
    [1, 3, 2],
    [4, 3, 1],
    [5, 6, 1]
]

print(min_sum_path(matrix))
print(min_sum_path_f(matrix)())
