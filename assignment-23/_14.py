# 14) Spiral Number Square
#      1   2   3   4
#     12  13  14   5
#     11  16  15   6
#     10   9   8   7


n = 4
matrix = [[0] * n for _ in range(n)]

num = 1
top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).rjust(4), end="")
    print()csx