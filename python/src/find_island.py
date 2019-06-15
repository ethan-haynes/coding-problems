matrix = [
    [1,1,0],
    [1,0,0],   
    [0,0,0]  
]

def fthst_node(graph, start):
    
    seen = set()
    indx = range(-1,2)

    while start:
        node = start.pop(0)
        
        seen.add(node)
        
        for n in [ (a+node[0],b+node[1]) for a in indx for b in indx ]:
            if n[0] < 0 or n[1] < 0:
                continue

            if len(graph) <= n[0] or len(graph[n[0]]) <= n[1]: 
                continue
            
            next_node = graph[n[0]][n[1]]
            
            if next_node != 1 and n not in seen:
                start.append(n)

    return node

print(fthst_node(matrix,[(0,0),(0,1),(1,0)]))
