def knapsack(items, S):
    max = { 'v': 0, 'path': [] }
    
    def place(items, path, s, v):
        for i, item in enumerate(items):
            w, val = item
            if s+w < S:
                place(items[:i] + items[i+1:], path + [item], s+w, val + v)
        
        if max['v'] < v:
            max['v'], max['path'] = v, path
    
    place(items, [], 0, 0)

    return max['path']


print(knapsack([(1,2),(3,4),(6,7),(2,3),(3,1),(1,1),(1,3),(4,4)], 10))
print(knapsack([(1,2),(3,4),(2,5),(6,7),(1,3),(2,3),(3,1)], 10))
