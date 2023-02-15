from data import TreeNode, printTree, drawTree
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    # swap the children
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)
    return root

tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
drawTree(printTree(tree1))
drawTree(printTree(invertTree(tree1), 0, [[]]))
