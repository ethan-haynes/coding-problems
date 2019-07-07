def sort_2d(m, reverse=True):
    row_l = len(m[-1])
    
    new_m = []
    
    arr = sorted(sum(m,[]), reverse=reverse)
    
    while len(arr):
        row = arr[:row_l]
        arr = arr[row_l:]
        new_m.append(row)
    
    return new_m

m = [
    [41, 45, 20, 21],
    [1 ,2, 3, 4],
    [30, 42, 43, 29],
    [16, 17, 19, 10]
]

m1 = sort_2d(m)

for row in m1:
    print(row)

m2 = sort_2d(m, reverse=False)

for row in m2:
    print(row)
