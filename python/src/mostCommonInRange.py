def mostCommonInRange(ranges):
    arr = [0]*101
    for r in ranges:
        start, end = r
        for i in range(start, end+1):
            arr[i-1900] += 1
    
    return max(range(len(arr)), key=lambda i: arr[i]) + 1900

print(mostCommonInRange([(1900,2000),(1945,1955),(1925,1965),(1981,1999)]))
