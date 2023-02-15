def uniquePath(m: int, n: int) -> int:
    row = [1] * n
    for j in range(m-1):
        below = row
        for i in range(n-1,-1,-1):
            row[i] = below[i]
            if i < n -1:
                row[i] += row[i+1]
    return row[0]
   
print(uniquePath(3,7)) # 28