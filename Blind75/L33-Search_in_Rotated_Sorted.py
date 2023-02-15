def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) -1
    while l <= r:
        m = (l + r)//2
        if nums[m] == target: return m
        # when only one portion going left by default
        # left sorted portion
        if nums[m] >= nums[l]:
            if target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        # right sorted portion
        else:
            if target > nums[r] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1
    return -1

nums1, t1 = [4,5,6,7,0,1,2], 0
nums2, t2 = [5,6,7,0,1,2,3], 3
print(search(nums1, t1)) #4
print(search(nums1, t2)) #-1
print(search(nums2, t2)) #6