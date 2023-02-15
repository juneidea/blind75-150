# pointer O n , O 3
def trap1(height: list[int]) -> int:

    if not height: return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res
# memory O 3n, O 2n
def trap2(height: list[int]) -> int:
    if not height: return 0
    maxLeft, maxRight = [], []
    l, r = 0, 0

    for h in height:
        maxLeft.append(l)
        if h > l:
            l = h

    for h in reversed(height):
        maxRight.append(r)
        if h > r:
            r = h
    maxRight.reverse()

    res = 0
    for idx, h in enumerate(height):
        waterTrap = min(maxLeft[idx], maxRight[idx])
        if (waterTrap > h):
            res += waterTrap - h

    return res
# recursion O nxl, O l
def trap3(height: list[int], level = None) -> int:
    if level == None:
        level = max(height)
    if level == 0:
        return 0
    prevMatch, atThisLevel = -1, 0
    for idx, h in enumerate(height):
        if h >= level:
            if prevMatch >= 0:
                atThisLevel += idx - prevMatch - 1
            prevMatch = idx
    return atThisLevel + trap3(height, level -1)


tropo1 = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap1(tropo1))
# print(trap2(tropo1))
# print(trap3(tropo1))



# def trap(height: list[int]) -> int:

# tropo1 = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(tropo1))