def countSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for j in range(2):
            l, r = i, i + j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
    return count

print(countSubstrings('aaab')) #7