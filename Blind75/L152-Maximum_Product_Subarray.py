def maxProduct(nums: list[int]) -> int:
    res = 0
    curMin, curMax = 1, 1

    for n in nums:
        tmp = n * curMax
        # after 0 n can be max or min
        curMax = max(tmp, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

print(maxProduct([-1,-2,-3,4])) # 24
print(maxProduct([-1,-2,-3,0,-2,4])) # 6