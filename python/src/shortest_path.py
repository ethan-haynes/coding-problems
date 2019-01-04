G = {'A': ['B', 'C', 'D'], 'B': ['D'], 'C': ['A','B'], 'D': ['C']}

def sp(g, m, n, memo={}):
    if not g: return []
    if m == n: return [n]

    if m not in memo:
        memo[m], paths = [None]*len(g), []
        
        for v in g:
            if v == m:
                for e in G[v]:
                    paths.append(sp(g,e,n, memo))
        memo[m] = [m] + min(paths, key=len)
    return memo[m]

print(sp(G, 'B', 'A', {}))
