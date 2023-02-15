from data import TreeNode, printTree, drawTree

def maxPathSum(root: TreeNode) -> int:
    res = [root.val]

    def dfs(root: TreeNode) -> int:
        if not root: return 0
        leftMax = max(0, dfs(root.left))
        rightMax = max(0, dfs(root.right))

        # compute max path sum WITH split
        res[0] = max(res[0], root.val + leftMax + rightMax)
        # compute max path sum without split
        return root.val + max(leftMax, rightMax)
    dfs(root)
    return res[0]

tree1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
drawTree(printTree(tree1))
print("Max Path Sum:", maxPathSum(tree1)) # 12