def trav(g, e, t, memo=None):
    if memo == None:
        memo = []
    if e in memo:
        return []

    l = []
    for i, node in enumerate(g[e]):
        cur = [(e,i,node[1])]
        if node[0] == t:
            l.append(cur)
        else:
            l.append(cur + trav(g,node[0],t, [e] + memo[:]))

    if len(l) == 0:
        return []

    return max(l, key=len)

def make_t(g):
    start = list(g.keys())[-1]
    return trav(g, start, start)

def swaps(people):
    '''
        1: [(2, "Adam")]
        2: [(1, "Brian"), (3, "Eric")]
        3: [(4, "Fred")]
        4: [(5, "Carl")]
        5: [(1, "Dan")]
    '''
    graph = {}
    swps = []
    for name, _from, to in people:
        if _from in graph:
            graph[_from].append((to, name))
        else:
            graph[_from] = [(to, name)]
    
    t = make_t(graph)
    
    while t:
        tmp = []
        
        for i in t:
            graph[i[0]].pop(i[1])
            tmp.append(i[2])
        
        swps.append(tmp) 
        t = trav(graph, start, start)

    return swps

print(swaps([
    ["Adam", 1, 2],
    ["Brian", 2, 1],
    ["Carl", 4, 5],
    ["Dan", 5, 1],
    ["Eric", 2, 3],
    ["Fred", 3, 4],       
]))
