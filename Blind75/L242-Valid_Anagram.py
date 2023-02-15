# Hash O 2n, O 2n
def isAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
# Sort O nlogn, O 1
def isAnagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s1, t1 = 'anagram', 'nagaram'
s2, t2 = 'rat', 'car'
print(isAnagram2(s1, t1)) # True
print(isAnagram2(s2, t2)) # False