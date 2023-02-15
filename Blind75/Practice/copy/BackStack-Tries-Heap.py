# L20
# def isValid(s: str) -> bool:

# s1 = "(){}[[[[[]]"
# s2 = "[]{{}}(())"
# print(isValid(s1)) # False
# print(isValid(s2)) # True



# L39
# def combinationSum(candidates: list[int], target: int) -> list[int]:

# cans1 = [2,3,6,7]
# target1 = 7
# print(combinationSum(cans1, target1)) # [[2, 2, 3], [7]]



# L79
# def exist(board: list[list[int]], word: str) -> bool:
        
# board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word1 = "ABCCED"
# word2 = "EECS"
# print(exist(board1, word1)) # True
# print(exist(board1, word2)) # True



# L208
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

# class Trie:
#     def __init__(self):
    
#     def insert(self, word: str) -> None:
                
#     def search(self, word: str) -> bool:

#     def startsWith(self, prefix: str) -> bool:
    
# trie1 = Trie()
# trie1.insert("apple")
# print(trie1.search("apple")) # True
# print(trie1.search("app")) # False
# print(trie1.startsWith("app")) # True



# L211
# search with . as any char
# class WordDictionary:
#     def __init__(self):

#     def addword(self, word: str) -> None:

#     def search(self, word: str) -> bool:

# dict1 = WordDictionary()
# dict1.addword("bad")
# dict1.addword("dad")
# dict1.addword("mad")
# print(dict1.search("pad")) # False
# print(dict1.search("bad")) # True
# print(dict1.search(".ad")) # True
# print(dict1.search("b..")) # True



# L212
# Word Search II
# class Trie:
#     def __init__(self):

#     def addWord(self, word: str) -> None:

# def findWords(board: list[list[str]], words: list[str]) -> list[str]:

# board1 = [["o", "a", "a", "n"],["e", "t", "a", "e"],["i","h","k","r"],["i","f","l","v"]]
# words1 = ["oath","pea","eat","rain"]
# print(findWords(board1, words1)) # ['oath', 'eat']



# L295
import heapq
# class MedianFinder:
#     def __init__(self):

#     def addNum(self, num: int) -> None:

#     def findMedian(self) -> float:

# stream1 = MedianFinder()
# stream1.addNum(3)
# stream1.addNum(2)
# print(stream1.findMedian()) # 2.5
# stream1.addNum(7)
# print(stream1.findMedian()) # 3
# stream1.addNum(4)
# print(stream1.findMedian()) # 3.5