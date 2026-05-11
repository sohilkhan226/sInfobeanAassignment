# 12) Hollow Diamond Numbers
#        1
#       2 2
#      3   3
#     4     4
#      3   3
#       2 2
#        1

n = 4

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end="")
        else:
            print(" ", end="")
    print()