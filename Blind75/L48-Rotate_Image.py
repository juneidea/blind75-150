def rotate(matrix: list[list[int]]) -> None:
    # Do not return anything, just modify input
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r-l):
            top, bottom = l, r
            topLeft = matrix[top][l+i]

            matrix[top][l+i] = matrix[bottom-i][l]
            matrix[bottom-i][l] = matrix[bottom][r-i]
            matrix[bottom][r-i] = matrix[top+i][r]
            matrix[top+i][r] = topLeft
        l += 1
        r -= 1

matrix1 = [ [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]]
rotate(matrix1)
print(matrix1)
