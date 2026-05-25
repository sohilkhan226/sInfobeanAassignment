# 1
# 22
# 3 3
# 4  4
# 55555


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print(i, end="")
        else:
            print(" ", end="")
    print()