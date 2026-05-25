# 123456789
#  1234567
#   12345
#    123
#     1


n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()