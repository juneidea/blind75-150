# Hashset O n, O n
def containsDuplicate1(nums: list[int]) -> bool:
    hash = set()
    for n in nums:
        if n in hash:
            return True
        else:
            hash.add(n)
    return False

# Sort O nlogn, O 1
def containsDuplicate2(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

nums1 = [1,2,3,4,1]
nums2 = [3,5,7,9,1]
print(containsDuplicate2(nums1)) # True
print(containsDuplicate2(nums2)) # False