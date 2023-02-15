# Use Result as Mem O 2n, O 1
def productExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    preFix, postFix = 1, 1
    for i in range(len(nums)):
        res[i] = preFix
        preFix *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postFix
        postFix *= nums[i]

    return res

nums1 = [1,2,3,4]
nums2 = [-1,1,0,3,-3]
print(productExceptSelf(nums1)) # [24, 12, 8, 6]
print(productExceptSelf(nums2)) # [0, 0, 9, 0, 0]