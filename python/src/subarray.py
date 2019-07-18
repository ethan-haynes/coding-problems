def subarray(arr):
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [arr]
    
    subarrs = []

    for i in range(n):
        subarrs.append(arr[i:])
        current = arr[i]
        remainder = arr[i+1:n-1]
        for subarr in subarray(remainder):
            subarrs.append([current] + subarr)
    return subarrs

print(subarray([1,2,3]))
