def isPalindrome(s: str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

def alphaNum(c: str) -> bool:
    return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

def isPalindrome1(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
print(isPalindrome1(s1)) # True
print(isPalindrome1(s2)) # False
print(isPalindrome1(s3)) # True