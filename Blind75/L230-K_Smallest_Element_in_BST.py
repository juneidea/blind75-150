from data import TreeNode, printTree, drawTree

def kthSmallest(root: TreeNode, k: int) -> int:
    n = 0
    stack = []
    cur = root

    while cur or len(stack) > 0:
        while cur:
            stack.append(cur)
            cur = cur.left
        # to the left most until cur = None
        # only move left after right or 1st time
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right

tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
drawTree(printTree(tree))
print(kthSmallest(tree, 4)) # 4
print(kthSmallest(tree, 3)) # 3