# DP rob or skip are sub problems, houses is a dynamic
# thread is 0, 0, for rob1, rob2, n, n+1
def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    
    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2

print(rob([1,2,3,1])) # 4
print(rob([1,2,3,1,2,3])) # 7