# L200
# def numIslands(grid: list[list[str]]) -> int:

# grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# print(numIslands(grid1)) #1
# grid2 = [["1","1","1","0","0"],["1","1","0","0","0"],["1","1","0","0","0"],["0","0","0","1","1"]]
# print(numIslands(grid2)) #2



# L133
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# def cloneGraph(node: Node) -> Node:

# n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
# n1.neighbors = [n2, n3]
# n2.neighbors = [n1, n4]
# n4.neighbors = [n2, n3]
# n3.neighbors = [n1, n4]

# c4 = cloneGraph(n4)
# print(n1.neighbors, n1.neighbors[0].val, n1.neighbors[1].val)
# print(n4.neighbors, n4.neighbors[0].val, n4.neighbors[1].val)
# print(c4.neighbors, c4.neighbors[0].val, c4.neighbors[1].val)



# L417
#      pac
# pac  []  atl
#      atl
# def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:

# heights1 = [[1,2,2,3,5],
#             [3,2,3,4,4],
#             [2,4,5,3,1],
#             [6,7,1,4,5],
#             [5,1,1,2,4]]
# print(pacificAtlantic(heights1)) # {(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)}



# L207
# def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:

# num1, preReq1 = 5, [[0,1],[0,2],[1,3],[1,4],[3,4]]
# num2, preReq2 = 3, [[0,1],[1,2],[2,0]]
# print(canFinish(num1, preReq1)) # True
# print(canFinish(num2, preReq2)) # False



# L323
# def countComponents(n: int, edges: list[list[int]]) -> int:

# print(countComponents(5, [[0,1],[1,2],[3,4]])) # 2



# L261
# def validTree(n, edges) -> bool:

# edges1, n1 = [[0,1],[0,2],[0,3],[1,4]], 5
# print(validTree(n1, edges1)) # True



# L269
# if words are not possible return ""
# def alienOrder(words: list[str]) -> str:
 
# words1 = ["wrt", "wrf", "er", "ett", "rftt"]
# print(alienOrder(words1)) # wertf