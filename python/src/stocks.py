def stocks(_list):
    n = len(_list)
    i = 1
    shares = 1
    profit = 0
    while i < n:
        if shares == 0:
            while _list[i-1] > _list[i]:
                i += 1
            shares = 1
            profit -= _list[i-1]
        if shares == 1:
            if _list[i-1] > _list[i]:
                profit += _list[i-1]
                shares = 0
        i += 1
    if shares == 1:
        profit += _list[n-1]
    return profit

print(stocks([1,2,3]))
print(stocks([1,2,1,3]))
print(stocks([1,2,1,4]))

    
