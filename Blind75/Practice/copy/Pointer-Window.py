# L125
# only alphanumeric char
# def isPalindrome(s: str) -> bool:

# s1 = "A man, a plan, a canal: Panama"
# s2 = "race a car"
# s3 = " "
# print(isPalindrome(s1)) # True
# print(isPalindrome(s2)) # False
# print(isPalindrome(s3)) # True



# L15
# return list of all possible [[3sum = 0],[3sum = 0]]
# def threeSum(nums: list[int]) -> list[list[int]]:

# nums1 = [-1,0,1,2,-1,-4]
# nums2 = [-3,3,4,-3,1,2]
# print(threeSum(nums1)) # [[-1, -1, 2], [-1, 0, 1]]
# print(threeSum(nums2)) # [[-3, 1, 2]]



# L11
# container most water
# def maxArea(height: list[int]) -> int:

# height1 = [1,8,6,2,5,4,8,3,7]
# print(maxArea(height1)) # 49



# L121
# def maxProfit(prices: list[int]) -> int:

# prices1 = [7,1,6,3,5,4]
# prices2 = [7,3,6,1,5,4]
# print(maxProfit(prices1)) # 5
# print(maxProfit(prices2)) # 4



# L3
# with no repeat
# def lengthOfLongestSubstring(s: str) -> int:

# s1 = "abcabcbb"
# s2 = "abcccccdef"
# print(lengthOfLongestSubstring(s1)) # 3
# print(lengthOfLongestSubstring(s2)) # 4



# L424
# def charactorReplacement(s: str, k: int) -> int:

# s1, k1 = "ABAB", 2
# s2, k2 = "AABABBA", 1
# print(charactorReplacement(s1, k1)) # 4
# print(charactorReplacement(s2, k2)) # 4



# L76
# minimum string that meet target
# def minWindow(s: str, t: str) -> str:

# s1, t1 = "ADOBECODEBANC", "ABC" # BANC
# print(minWindow(s1, t1))