# 1
# 11
# 1*1
# 1**1
# 11111

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("1", end="")
        else:
            print("*", end="")
    print()