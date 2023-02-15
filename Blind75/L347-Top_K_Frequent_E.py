def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            if len(res) < k:
                res.append(n)
    return res

nums1, k1 = [1,1,1,2,2,3,11], 2
nums2, k2 = [4,5,6,1,2,3,3,3,2,1,4,5,6], 3
print(topKFrequent(nums1, k1)) # [1, 2]
print(topKFrequent(nums2, k2)) # [3, 4, 5]