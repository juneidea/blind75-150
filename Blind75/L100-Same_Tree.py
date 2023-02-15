from data import TreeNode

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if (not p or not q) or p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

n1 = TreeNode(1, TreeNode(2), TreeNode(3))
n2 = TreeNode(1, TreeNode(2), TreeNode(3))
n3 = TreeNode(1, TreeNode(2, TreeNode(3)))
print(isSameTree(n1, n2)) # True
print(isSameTree(n1, n3)) # False