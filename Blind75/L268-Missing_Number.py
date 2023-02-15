def missingNum(nums: list[int]) -> int:
    res = len(nums)
    for i in range(len(nums)):
        # res = res ^ nums[i] ^ i
        res += i - nums[i]
    return res

print(missingNum([4,3,2,1,0,5,7])) # 6