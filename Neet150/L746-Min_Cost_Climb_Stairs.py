def minCostClimb(cost: list[int]) -> int:
    cost.append(0)
    for i in range(len(cost) -3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])

cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimb(cost1)) # 15
print(minCostClimb(cost2)) # 6