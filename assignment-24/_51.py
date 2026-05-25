# 55555
# 4__4
# 3_3
# 22
# 1

n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print(i, end="")
        else:
            print("_", end="")
    print()