# Window O n, O n
def charactorReplacement1(s: str, k: int) -> int:
    count = {}
    l, longest = 0, 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        # count.values O n
        while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        longest = max(longest, r-l+1)
    return longest
# Add max memory O n, O 1
def charactorReplacement2(s: str, k: int) -> int:
    count = {}
    l, longest, maxFreq = 0, 0, 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxFreq = max(maxFreq, count[s[r]])
        # maxFreq O 1
        while (r-l+1) - maxFreq > k:
            count[s[l]] -= 1
            l += 1
        longest = max(longest, r-l+1)
    return longest


s1, k1 = "ABAB", 2
s2, k2 = "AABABBA", 1
print(charactorReplacement2(s1, k1)) # 4
print(charactorReplacement2(s2, k2)) # 4