def getSum(a: int, b: int) -> int:
    while b != 0:
        tmp = (a&b)<<1
        a = a^b
        b = tmp
    return a

print(getSum(9,11))