#  5
# 54
# 543
# 5432
# 54321

n = 5
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end="")
    print()