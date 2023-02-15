from data import TreeNode, printTree, drawTree
from collections import deque
# L226
# def invertTree(root: TreeNode) -> TreeNode:

# tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# drawTree(printTree(tree1))
# drawTree(printTree(invertTree(tree1), 0, [[]]))



# L104
# def maxDepth(root: TreeNode) -> int:

# tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# print(printTree(tree1))
# print(maxDepth(tree1)) # 3



# L100
# def isSameTree(p: TreeNode, q: TreeNode) -> bool:

# n1 = TreeNode(1, TreeNode(2), TreeNode(3))
# n2 = TreeNode(1, TreeNode(2), TreeNode(3))
# n3 = TreeNode(1, TreeNode(2, TreeNode(3)))
# print(isSameTree(n1, n2)) # True
# print(isSameTree(n1, n3)) # False



# L572
# def isSubTree(s: TreeNode, t: TreeNode) -> bool:

# n1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)))
# n2 = TreeNode(2, TreeNode(3), TreeNode(4))
# n3 = TreeNode(1, TreeNode(2, TreeNode(3)))
# print(isSubTree(n1, n2)) # True
# print(isSubTree(n1, n3)) # False



# L235
# def lowestCommonAncestor(root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:

# tree = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
# drawTree(printTree(tree))
# node2 = tree.left
# node8 = tree.right
# print('ancestor 2 & 8 is')
# print(lowestCommonAncestor(tree, node2, node8).val)
# node7 = tree.right.left
# node9 = tree.right.right
# print('ancestor 7 & 9 is')
# print(lowestCommonAncestor(tree, node7, node9).val)



# L102
# def levelOrder(root: TreeNode) -> list[list[int]]:

# tree = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
# drawTree(printTree(tree))
# print(levelOrder(tree)) # [[6], [2, 8], [1, 4, 7, 9], [3, 5]]



# L98
# def isValidBST(root: TreeNode) -> bool:

# tree = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
# drawTree(printTree(tree))
# print(isValidBST(tree)) # True



# L230
# def kthSmallest(root: TreeNode, k: int) -> int:

# tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
# drawTree(printTree(tree))
# print(kthSmallest(tree, 4)) # 4
# print(kthSmallest(tree, 3)) # 3



# L105
# def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:

# preorder1 = [3,9,20,15,7]
# inorder1 = [9,3,15,20,7]
# drawTree(printTree(buildTree(preorder1, inorder1)))



# L124
# def maxPathSum(root: TreeNode) -> int:

# tree1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
# drawTree(printTree(tree1))
# print("Max Path Sum:", maxPathSum(tree1)) # 12



# L297
# class Codec:
#     def serialize(self, root: TreeNode) -> str:

#     def deserialize(self, data:str) -> TreeNode:

# tree1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
# drawTree(printTree(tree1))
# serial1 = Codec.serialize(Codec, tree1)
# print(serial1) # 1,2,N,N,3,4,N,N,5,N,N
# deserial below
# drawTree(printTree(Codec.deserialize(Codec, serial1), 0, [[]]))