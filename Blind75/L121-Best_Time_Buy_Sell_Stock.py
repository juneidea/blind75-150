def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1 # l-buy, r-sell
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP

prices1 = [7,1,6,3,5,4]
prices2 = [7,3,6,1,5,4]
print(maxProfit(prices1))
print(maxProfit(prices2))