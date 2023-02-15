from data import TreeNode, printTree, drawTree
from collections import deque

def levelOrder(root: TreeNode) -> list[list[int]]:
    res = []
    q = deque([root])

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res

tree = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
drawTree(printTree(tree))
print(levelOrder(tree)) # [[6], [2, 8], [1, 4, 7, 9], [3, 5]]