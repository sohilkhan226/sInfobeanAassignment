# 20) Continuous Diamond Numbers
#            1
#           2 3
#          4 5 6
#         7 8 9 10
#          4 5 6
#           2 3
#            1


n = 4
num = 1

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

num = n
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    start = num - i + 1
    for j in range(i):
        print(start + j, end=" ")
    num -= i
    print()