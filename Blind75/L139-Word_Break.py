# DP dictionary is the sub problem, string is the dynamic
def wordBreak(s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s)+1)
    # Thread
    dp[len(s)] = True
    # only last dp and the beginning of each word that is match are dp = True
    # overlap or separate word will pick up False from dp
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i] == True: break
    return dp[0]

print(wordBreak('neetcode', ['leet', 'neet', 'code'])) # True