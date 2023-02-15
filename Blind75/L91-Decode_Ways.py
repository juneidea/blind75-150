# 0, 1-9, 10-26 are sub problems, string is a dynamic
# thread len(s): 1
# Dynamic Recursion
def numDeCodings(s: str) -> int:
    # cache
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
            
        res = dfs(i+1)
        if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            res += dfs(i+2)
        dp[i] = res
        return res

    return dfs(0)

# Dynamic
def numDeCodings1(s: str) -> int:
    dp = {len(s): 1}

    for i in range(len(s)-1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]

        if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            dp[i] += dp[i+2]
    return dp[0]

print(numDeCodings1('121')) # 3
print(numDeCodings('127')) # 2
print(numDeCodings1('1201')) # 1