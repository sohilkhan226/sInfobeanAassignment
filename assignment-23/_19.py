
# 19) Reverse Number Cross
#     5   5
#      4 4
#       3
#      4 4
#     5   5


n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i or j == n - i + 1:
            print(n - i + 1, end="")
        else:
            print(" ", end="")
    print()