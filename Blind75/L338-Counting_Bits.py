def countBits(n: int) -> list[int]:
    dp = [0] * (n+1)
    pow = 1
    for i in range(1, n+1):
        nextPow = pow * 2
        if i == nextPow:
            pow = nextPow
        dp[i] = 1 + dp[i-pow]
    return dp

print(countBits(16))