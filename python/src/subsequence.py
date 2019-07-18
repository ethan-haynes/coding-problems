def subsequence(arr):
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [arr]

    subs = []

    for i in range(n):
        current = arr[i]
        remainder = arr[i+1:]
        subs.append([current])
        for sub in subsequence(remainder):
            subs.append([current] + sub)
    return subs

print(subsequence([1,2,3]))
