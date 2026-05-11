# 9) Hollow Diamond Square
#     ***********
#     ****   ****
#     ***     ***
#     **       **
#     *         *
#     *         *
#     **       **
#     ***     ***
#     ****   ****
#     ***********


n = 5
total = 2 * n + 1

for i in range(1, total + 1):
    for j in range(1, total + 1):
        if i <= n:
            if j <= n - i + 1 or j >= n + i:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            row = i - n
            if j <= row or j >= total - row + 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()