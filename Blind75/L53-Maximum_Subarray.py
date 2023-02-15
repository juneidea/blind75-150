def maxSubArray(nums: list[int]) -> int:
    maxSub = nums[0]
    curSum = 0
    for n in nums:
        curSum += n
        if curSum < 0:
            curSum = 0
        maxSub = max(maxSub, curSum)
    return maxSub

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6       