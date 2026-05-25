# 123456789
#  1+++++7
#   1+++5
#    1+3
#     1


n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if i == n or i == 1 or j == 1 or j == 2 * i - 1:
            print(j, end="")
        else:
            print("+", end="")
    print()