# DP coins are sub problems and amount is a dynamic 0 -> 7
# thread $0 = 0, $1 = 1, $2 = 2coins, $3 = 1
# so 1 current coin + remain
def coinChange(coins: list[int], amount: int) -> int:
    dp = [amount] * (amount+1)
    dp[0] = 0

    for a in range(1, amount+1):
        for c in coins:
            if a - c >= 0:
# min dp[a] find the least, 1 is the current coin, dp[a-c] is the remain should calculated 
                dp[a] = min(dp[a], 1 + dp[a-c])
    print(dp)
    return dp[amount]

coins1, amount1 = [1,3,4,5], 7

print(coinChange(coins1, amount1)) # 2