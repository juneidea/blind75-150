def findMin(nums: list[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1
    while nums[l] > nums[r]:
        m = (l + r)//2
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m
    return min(res, nums[l])

nums1 = [3,4,5,1,2]
nums2 = [7,1,2,3,4,5,6]
print(findMin(nums1)) # 1
print(findMin(nums2)) # 1