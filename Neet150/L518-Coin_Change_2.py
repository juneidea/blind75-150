def coinChange(coins: list[int], amount: int) -> int:
    comb = [0]
    def dfs(i, total):
        if i == len(coins) or total > amount:
            return
        if total == amount:
            comb[0] += 1
            print(i, total, comb[0])
            return
        dfs(i, total + coins[i])
        dfs(i+1, total)
    dfs(0, 0)
    return comb[0]

coins1, amount1 = [1,2,5], 5
coins2, amount2 = [1,3,4], 7
print(coinChange(coins1, amount1)) # 4
print(coinChange(coins2, amount2)) # 5