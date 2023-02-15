def isInterleave(a: str, b: str, c: str) -> bool:
    if len(a) + len(b) != len(c): return False
    dp = [[False] * (len(b)+1) for i in range(len(a)+1) ]
    dp[len(a)][len(b)] = True # a-vertical b-horizontal
    for i in range(len(a), -1, -1):
        for j in range(len(b), -1, -1):
            # last and condition to maintain the link relation
            if j < len(b) and c[i+j] == b[j] and dp[i][j+1] == True:
                dp[i][j] = True
            if i < len(a) and  c[i+j] == a[i] and dp[i+1][j] == True:
                dp[i][j] = True
    return dp#[0][0]

# def isInterleave(a: str, b: str, c: str) -> bool:
#     dp = {}
#     def dfs(i, j):
#         if i == len(a) and j == len(b):
#             return True
#         if (i, j) in dp:
#             return dp[(i, j)]

#         if i < len(a) and c[i+j] == a[i] and dfs(i+1, j) == True:
#             return True
#         if j < len(b) and c[i+j] == b[j] and dfs(i, j+1) == True:
#             return True
#         dp[(i, j)] = False
#         return False
#     return dfs(0, 0)

a1, b1, c1 = 'aabcc', 'dbbca', 'aadbbcbcac'
print(isInterleave(a1, b1, c1))