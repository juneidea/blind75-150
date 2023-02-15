def longestComSub(text1: str, text2: str) -> int:
    # text1 vertical, text2 horizontal
    dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]
    for j in range(len(text1)-1,-1,-1):
        for i in range(len(text2)-1,-1,-1):
            if text2[i] == text1[j]:
                dp[j][i] = dp[j+1][i+1] + 1
            else:
                dp[j][i] = max(dp[j+1][i], dp[j][i+1])

    return dp[0][0]

print(longestComSub('abcde', 'ace')) # 3