from data import TreeNode
def isSubTree(s: TreeNode, t: TreeNode) -> bool:
    if not t: return True
    if not s: return False
    if sameTree(s, t): 
        return True
    return isSubTree(s.left, t) or isSubTree(s.right, t)

def sameTree(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if (s and t) and s.val == t.val:
        return sameTree(s.left, t.left) and sameTree(s.right, t.right)

    return False

n1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)))
n2 = TreeNode(2, TreeNode(3), TreeNode(4))
n3 = TreeNode(1, TreeNode(2, TreeNode(3)))
print(isSubTree(n1, n2)) # True
print(isSubTree(n1, n3)) # False