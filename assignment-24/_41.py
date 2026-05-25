# 54321
# 5432
# 543
# 54
# 5
# 1
# 12
# 123
# 1234
# 12345


n = 5
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end="")
    print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()