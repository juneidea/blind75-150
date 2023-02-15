def firstMissingPositive(A: list[int]) -> int:
    for i in range(len(A)):
        if A[i] < 0:
            A[i] *= -1

    for i in range(len(A)):
        val = abs(A[i])
        if 1 <= val <= len(A):
            if A[val - 1] > 0:
                A[val - 1] *= -1
            elif A[val - 1] == 0:
                A[val - 1] = -1 ^ (len(A) + 1)
    
    for i in range(1, len(A) + 1):
        if A[i - 1] >= 0:
            return i
    return len(A) + 1

A1 = [1,2,0]
A2 = [3,4,-1,1]
A3 = [7,8,9,11,12]
A4 = [6,1,5,2,4,3]
print(firstMissingPositive(A1))
print(firstMissingPositive(A2))
print(firstMissingPositive(A3))
print(firstMissingPositive(A4))