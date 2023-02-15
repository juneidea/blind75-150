from collections import deque
from data import TreeNode, printTree, drawTree
# Recursive O n
def maxDepth1(root: TreeNode) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth1(root.left), maxDepth1(root.right))
# Breadth First O n
def maxDepth2(root: TreeNode) -> int:
    if not root:
        return 0
    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level
# Depth First O n
def maxDepth3(root: TreeNode) -> int:
    level = 0
    stack =[[root, 1]]
    while stack:
        node, depth = stack.pop()
        if node:
            level = max(level, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return level

tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(printTree(tree1))
print(maxDepth1(tree1))