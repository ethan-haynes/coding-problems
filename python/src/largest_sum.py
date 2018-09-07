def largest_sum(arr):
    largest = { 'sum': None }

    def _find(start):
        s = 0
        for i in range(start, len(arr)):
            s += arr[i]
            if largest['sum'] == None or largest['sum'] < s:
                largest['sum'] = s
            _find(start + 1)
    
    _find(0)
    
    return largest['sum']

print(largest_sum([2,-8,3,-2,4,-10]))
