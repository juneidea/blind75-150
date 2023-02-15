from data import TreeNode, printTree, drawTree

def lowestCommonAncestor(root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur

tree = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
drawTree(printTree(tree))
node2 = tree.left
node8 = tree.right
print('ancestor 2 & 8 is')
print(lowestCommonAncestor(tree, node2, node8).val)
node7 = tree.right.left
node9 = tree.right.right
print('ancestor 7 & 9 is')
print(lowestCommonAncestor(tree, node7, node9).val)