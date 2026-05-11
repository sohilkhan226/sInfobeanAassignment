# 17) Hollow Hourglass
#     * * * * *
#       *     *
#         * *
#           *
#         * *
#       *     *
#     * * * * *


n = 5
for i in range(1, n + 1):
    for j in range(i - 1):
        print("  ", end="")
    for j in range(1, 2 * (n - i + 1)):
        if i == 1 or i == n or j == 1 or j == 2 * (n - i + 1) - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i - 1):
        print("  ", end="")
    for j in range(1, 2 * (n - i + 1)):
        if i == 1 or i == n or j == 1 or j == 2 * (n - i + 1) - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()