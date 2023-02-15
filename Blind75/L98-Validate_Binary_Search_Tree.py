from data import TreeNode, printTree, drawTree

def isValidBST(root: TreeNode) -> bool:
    def valid(node: TreeNode, left: int, right: int) -> bool:
        if not node:
            return True
        if not(node.val > left and node.val < right):
            return False
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    return valid(root, float("-inf"), float("inf"))

tree = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
drawTree(printTree(tree))
print(isValidBST(tree)) # True