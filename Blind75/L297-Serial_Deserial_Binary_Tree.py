from data import TreeNode, printTree, drawTree

class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []

        def dfs(node: TreeNode):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data:str) -> TreeNode:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

tree1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
drawTree(printTree(tree1))
serial1 = Codec.serialize(Codec, tree1)
print(serial1) # 1,2,N,N,3,4,N,N,5,N,N
drawTree(printTree(Codec.deserialize(Codec, serial1), 0, [[]]))