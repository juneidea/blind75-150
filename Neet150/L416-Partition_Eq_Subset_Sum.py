def isPartitionSub(nums: list[int]) -> bool:
    half = sum(nums)/2
    if not half.is_integer(): return False
    halfSet = set()
    halfSet.add(0)

    for n in nums:
        if n == half: return True
        newSet = set()
        for h in halfSet:
            print(n, h)
            if h + n == half:
                return True
            elif h + n < half:
                newSet.add(h + n)
                newSet.add(h)
        halfSet = newSet
    return False

nums1 = [1,5,9,2,5]
nums2 = [1,2,3,8]
print(isPartitionSub(nums1)) # True
print(isPartitionSub(nums2)) # False