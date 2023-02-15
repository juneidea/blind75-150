def longestPalin(s: str) -> str:
    res, resLen = "", 0
    for i in range(len(s)):
        # for l, r => i, i = odd / i, i+1 = even length
        for j in range(2):
            l, r = i, i+j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
    return res

print(longestPalin("babbad")) # abba