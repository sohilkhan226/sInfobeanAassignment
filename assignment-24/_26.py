# 1
# 10
# 1 1
# 1  0
# 10101

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            if (i + j) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        else:
            print(" ", end="")
    print()