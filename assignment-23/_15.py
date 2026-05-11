# 15) Zig-Zag Star
#     *   *   *
#       *   *
#     *   *   *


n = 3
for i in range(1, n + 1):
    for j in range(1, n * 4):
        if i == 1 and (j % 4 == 1):
            print("*", end="")
        elif i == 2 and (j % 4 == 3):
            print("*", end="")
        elif i == 3 and (j % 4 == 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()