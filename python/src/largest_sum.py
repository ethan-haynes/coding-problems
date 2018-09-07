def largest_sum(arr):
    largest, memo = { 'sum': None }, {}
    
    def _find(start):
        s = 0
        for i in range(start, len(arr)):
            key = f'{start},{i}'
            if key not in memo:
                s += arr[i]
                memo[key] = s
                _find(start + 1)
            else:
                s = memo[key]

            if largest['sum'] == None or largest['sum'] < s:
                largest['sum'] = s
    
    _find(0)
    
    return largest['sum']

print(largest_sum([2,-8,3,-2,4,-10]))
print(largest_sum([2,-8,3,-2,4,-10,2,-8,3,-2,4,-10,2,-8,3,-2,4,-10,2,-8,3,-2,4,-10]))
