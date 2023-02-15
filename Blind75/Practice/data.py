class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode) -> list[int]:
    res = []
    if head:
        res.append(head.val)
        cur = head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
    return print(res)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def printTree(root: TreeNode, i = 0, res = [[]], d = 0) -> list[list[int]]:
    # base recursive
    if not root:
        res[i].append(0)
        return None
    # find max depth
    if d == 0:
        d = maxDepth(root)

    queue = []
    res[i].append(root.val)
    if root.left or root.right:
        i += 1
        if len(res) < i + 1:
            res.append([])
        queue.append(root.left)
        queue.append(root.right)
    elif i + 2 <= d:
        i += 1
        if len(res) < i + 1:
            res.append([0, 0])
        else:
            res[i].append(0)
            res[i].append(0)

    while len(queue) > 0:
        printTree(queue[0], i, res, d)
        queue.pop(0)

    return res

def drawTree(tree: list[list[int]]) -> str:
    s = 0
    for i in range(len(tree)-1, -1, -1):
        number, lines = "",  ""
        line = "/"
        for n in tree[i]:
            node = " " if n == 0 else str(n)
            number = number + " "*(2**s-1) + node + " "*(s+1)
            line = "\\" if line == "/" else "/" 
            l = " " if n == 0 else line
            lines = lines + " "*(2**s-1) + l + " "*(s+1)
        s += 1
        print(number)
        print(lines) if i != 0 else None
