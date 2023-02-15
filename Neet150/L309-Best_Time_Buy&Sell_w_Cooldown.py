def maxProfit(prices: list[int]) ->int:
    # caching
    dp = {} # key = (i, buying), value = max profit
    def dfs(i, buying):
        if i >= len(prices): return 0
        if (i, buying) in dp:
            return dp[(i, buying)]

        cooldown = dfs(i+1, buying)
        if buying:
            buy = dfs(i+1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]
    return dfs(0, True)


prices1 = [1,2,3,1,3]
print(maxProfit(prices1)) #3



def maxProfit(prices: list[int]) ->int:
    cache = {} # (i, buying) - maxProfit

    def dfs(i: int, buying: bool) ->int:
        if i >= len(prices): return 0
        if (i, buying) in cache:
            return cache[(i, buying)]

        wait = dfs(i+1, buying)
        if buying:
            buy = dfs(i+1, not buying) - prices[i]
            cache[(i, buying)] = max(wait, buy)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            cache[(i, buying)] = max(wait, sell)
        return cache[(i, buying)]
    return dfs(0, True)

prices1 = [1,2,3,1,3]
print(maxProfit(prices1)) #3