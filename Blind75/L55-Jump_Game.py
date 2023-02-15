# brute force recursive O n^n
def canJump1(nums: list[int]) -> bool:
    # add cache for O n^2
    dp = {}
    def solve(idx: int) -> bool:
        if idx == len(nums) - 1:
            return True
        reach = idx + nums[idx]
        for i in range(idx + 1, reach + 1): 
            if i in dp:
                print(i, dp)
                continue
            if solve(i):
                    return True
        dp[idx] = False
        return False

    return solve(0)
# dynamic program use a list
def canJump2(nums: list[int]) -> bool:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] - 1, nums[i])
        if dp[i] == 0 and i < n:
            return False
    return True
# greedy backward goal moving
def canJump3(nums: list[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

jumps1 = [3,2,1,0,4] # False
jumps2 = [2,3,1,1,4] # True
print(canJump3(jumps1))
print(canJump3(jumps2))