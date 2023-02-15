def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {} # val : index
 
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

nums1 = [2,7,11,15]
nums2 = [2,1,5,3]
# return [idx, idx] that sum up to the target
print(twoSum(nums1, 9)) # [0, 1]
print(twoSum(nums2, 4)) # [1, 3]