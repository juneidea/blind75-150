from data import TreeNode, printTree, drawTree

def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree( preorder[1:mid+1], inorder[:mid] )
    root.right = buildTree( preorder[mid+1:], inorder[mid+1:] )
    return root

preorder1 = [3,9,20,15,7]
inorder1 = [9,3,15,20,7]
drawTree(printTree(buildTree(preorder1, inorder1)))