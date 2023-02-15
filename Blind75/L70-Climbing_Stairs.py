# DP climbing 1 or 2 are sub problems, stairs is a dynamic
def climbStairs(n:int) -> int:
    # thread
    one, two = 1, 1
    for i in range(n-1):
        temp = one + two
        two = one
        one = temp
    return one

print(climbStairs(1)) # 1
print(climbStairs(2)) # 2
print(climbStairs(3)) # 3
print(climbStairs(4)) # 5
print(climbStairs(5)) # 8