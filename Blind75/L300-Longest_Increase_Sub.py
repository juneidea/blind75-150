# DP skipping is a sub problem, numbers is a dynamic
def lengthOfLis(nums: list[int]) -> int:
    # Thread 1 at the last nums
    LIS = [1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)

print(lengthOfLis([10,9,2,5,3,7,20,18])) # 4
print(lengthOfLis([0,3,1,6,2,2,7])) # 4
print(lengthOfLis([10,9,4,8,3,7,20,18])) # 3
print(lengthOfLis([0,1,0,3,2,3])) # 4