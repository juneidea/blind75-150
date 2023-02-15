# L217
# def containsDuplicate(nums: list[int]) -> bool:

# nums1 = [1,2,3,4,1]
# nums2 = [3,5,7,9,1]
# print(containsDuplicate(nums1)) # True
# print(containsDuplicate(nums2)) # False



# L242
# def isAnagram(s: str, t: str) -> bool:

# s1, t1 = 'anagram', 'nagaram'
# s2, t2 = 'rat', 'car'
# print(isAnagram(s1, t1)) # True
# print(isAnagram(s2, t2)) # False



# L1
# return [idx, idx] that sum up to the target
# def twoSum(nums: list[int], target: int) -> list[int]:

# nums1 = [2,7,11,15]
# nums2 = [2,1,5,3]
# print(twoSum(nums1, 9)) # [0, 1]
# print(twoSum(nums2, 4)) # [1, 3]



# L49
# from typing import DefaultDict
# def groupAnagrams(strs: list[str]) -> list[list[str]]:

# str1 = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(str1)) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



# L347
# def topKFrequent(nums: list[int], k: int) -> list[int]:

# nums1, k1 = [1,1,1,2,2,3,11], 2
# nums2, k2 = [4,5,6,1,2,3,3,3,2,1,4,5,6], 3
# print(topKFrequent(nums1, k1)) # [1, 2]
# print(topKFrequent(nums2, k2)) # [3, 4, 5]



# L238
# Use Result as Mem O 2n, O 1
# def productExceptSelf(nums: list[int]) -> list[int]:

# nums1 = [1,2,3,4] 
# nums2 = [-1,1,0,3,-3] 
# print(productExceptSelf(nums1)) # [24, 12, 8, 6]
# print(productExceptSelf(nums2)) # [0, 0, 9, 0, 0]



# L271
# [] to string then string to []
# def encode(strs: list[str]) -> str:

# def decode(strs: str) -> list[str]:

# strs1 = ["leetcodelove", "leet", "code", "love"]
# print(encode(strs1)) # 12#leetcodelove4#leet4#code4#love
# print(decode(encode(strs1)))



# L128
# def longestConsecutive(nums: list[int]) -> int:

# nums0 = []
# nums1 = [9]
# nums2 = [100,4,200,3,1,2]
# print(longestConsecutive(nums0)) # 0
# print(longestConsecutive(nums1)) # 1
# print(longestConsecutive(nums2)) # 4