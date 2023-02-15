def twoSum(numbers: list[int], target: int) -> list[int]:
    l , r = 0 , len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l+1, r+1]
    return []

numbers1 = [1,3,4,5,7,10,11]
print(twoSum(numbers1, 9))