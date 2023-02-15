def num1Bit(n: int) -> int:
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res

print(num1Bit(5)) # 2

def num2Bit(n: int) -> int:
    res = 0
    while n:
        n &= (n-1)
        res += 1
    return res

print(num2Bit(15)) # 4
