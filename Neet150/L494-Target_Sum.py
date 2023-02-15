def targetSum(nums: list[int], target: int) -> int:
    count = [0]
    def dfs(i, total):
        if i == len(nums):
            if total == target:
                count[0] += 1
            return

        dfs(i+1, total+nums[i])
        dfs(i+1, total-nums[i])
    dfs(0,0)
    return count[0]

nums1, target1 = [1,1,1,1,1], 3
nums2, target2 = [1,2,1,2,1], 3
print(targetSum(nums1, target1)) # 5
print(targetSum(nums2, target2)) # 5