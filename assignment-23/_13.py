# 13) Number X Pattern
#     1   5
#      2 4
#       3
#      2 4
#     1   5

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i:
            print(j, end="")
        elif j == n - i + 1:
            print(j, end="")
        else:
            print(" ", end="")
    print()