class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
    oldToNew = {}
    
    def dfs(node: Node):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    
    return dfs(node) if node else None    

n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n3]
n2.neighbors = [n1, n4]
n4.neighbors = [n2, n3]
n3.neighbors = [n1, n4]

c4 = cloneGraph(n4)
print(n1.neighbors, n1.neighbors[0].val, n1.neighbors[1].val)
print(n4.neighbors, n4.neighbors[0].val, n4.neighbors[1].val)
print(c4.neighbors, c4.neighbors[0].val, c4.neighbors[1].val)
