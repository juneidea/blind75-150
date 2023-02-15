#return list of all possible [[3sum = 0],[3sum = 0]]
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

nums1 = [-1,0,1,2,-1,-4]
nums2 = [-3,3,4,-3,1,2]
print(threeSum(nums1)) # [[-1, -1, 2], [-1, 0, 1]]
print(threeSum(nums2)) # [[-3, 1, 2]]