class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addword(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    # no children or not reach goal
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            # dfs goal to find cur.endOfWord == True
            return cur.endOfWord

        return dfs(0, self.root)

dict1 = WordDictionary()
dict1.addword("bad")
dict1.addword("dad")
dict1.addword("mad")
print(dict1.search("bad")) # True
print(dict1.search(".ad")) # True
print(dict1.search("b..")) # True
