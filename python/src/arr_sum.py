def arr_sum(arr):
    if not arr: return 0
    memo = {}

    def _sum(i, j, s):
        if i == j: return -float('inf'), (i,j) 
        key = f'{i},{j}'
        if key not in memo:
            memo[key] = max((s, (i,j)),
                        _sum(i+1, j, s - arr[i]),
                        _sum(i, j-1, s - arr[j-1])
                    )
        return memo[key]
    s, (i,j) = _sum(0, len(arr), sum(arr))
    return arr[i:j]

print(arr_sum([1,2,3,4,5,6]))
print(arr_sum([1,-2,3,-4,9,-2,4,-7,2]))
