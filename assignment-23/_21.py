# 21) Hollow Pyramid (Practice)
#             *
#            * *
#           *   *
#          *     *
#         *********


n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if i == 1 or i == n or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()