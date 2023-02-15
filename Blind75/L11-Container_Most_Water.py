# Brute O n^2, O 1
def maxArea1(height: list[int]) -> int:
    res = 0
    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            if( area > res):
                res = area
    return res
# Pointers O n, O 1
def maxArea2(height: list[int]) -> int:
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        if(height[l] <= height[r]):
            l += 1
        else:
            r -= 1
    return res

height1 = [1,8,6,2,5,4,8,3,7]
print(maxArea1(height1))
print(maxArea2(height1))