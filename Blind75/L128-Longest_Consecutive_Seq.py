# Set O n, O n
def longestConsecutive(nums: list[int]) -> int:
    if not len(nums): return 0
    numSet = set(nums)
    longest = 1
    for n in nums:
        # check for the start of sequence
        if (n - 1) not in numSet:
            seq = 1
            while (n + seq) in numSet:
                seq += 1
            longest = max(longest, seq)
                
    return longest
    
nums0 = []
nums1 = [9]
nums2 = [100,4,200,3,1,2]
print(longestConsecutive(nums0))
print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
