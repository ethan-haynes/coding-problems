def comp(arr):
    n = len(arr)
    m = len(arr[-1])
    get_indices = lambda arr: [ (i,j) for j in range(m) for i in range(n) ]
    get_index = lambda tup: arr[tup[0]][tup[1]]

    for i, tup in enumerate(sorted(get_indices(arr), key=get_index)):
        arr[tup[0]][tup[1]] = i + 1

arr = [[7,6],[4,9]]
comp(arr), print(arr)
