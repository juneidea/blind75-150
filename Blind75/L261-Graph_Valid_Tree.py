def validTree(n, edges):
    if not n:
        return True
    
    adj = { i:[] for i in range(n) }
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()
    def dfs(i, prev):
        if i in visit:
            return False
        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True
    # visit all node mean all connected
    return dfs(0, -1) and n == len(visit)

edges1, n1 = [[0,1],[0,2],[0,3],[1,4]], 5
print(validTree(n1, edges1))