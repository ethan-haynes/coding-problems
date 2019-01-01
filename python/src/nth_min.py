def min(arr=[], m=1):
    if len(arr) and m > 0:
        num = None
        
        while(m != 0):
            for i in range(len(arr)):
                if arr[i] < arr[0]: arr[i] = arr[0]
            num = arr.pop(0)
            m -= 1

        return num

def min2(arr=[], m=1):
    def __partition(arr):
        l, a1, a2 = len(arr), [], []
        mid = l//2
        while(l):
            l -= 1
            if arr[l] < arr[mid]: a1.append(arr[l])
            elif arr[l] > arr[mid]: a2.append(arr[l])
        return arr[mid],a1,a2

    if len(arr) and m > 0:
        target = None
        while(not target):
            data, left, right = __partition(arr)
            len_l = len(left)
            if len_l > m:
                arr = left
            elif len_l < m:
                arr, m = right, m - len_l - 1
            else:
                target = data

        return target

print(min([3,2,6,5,10,21,15], 3))
print(min2([3,2,6,5,10,21,15], 3))
