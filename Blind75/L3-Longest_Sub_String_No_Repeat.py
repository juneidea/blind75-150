def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l, longest = 0, 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        longest = max(longest, r-l+1)
    return longest

s1 = "abcabcbb"
s2 = "abcccccdef"
print(lengthOfLongestSubstring(s1)) # 3
print(lengthOfLongestSubstring(s2)) # 4