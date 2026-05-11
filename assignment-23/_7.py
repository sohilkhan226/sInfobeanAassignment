# 7) Reverse Number Triangle
#     - - - -
#     2 - - -
#     4 3 - -
#     6 5 4 -
#     8 7 6 5


n = 5
for i in range(0, n):
    num = 2 * i
    for j in range(1, n):
        if j <= i:
            print(num, end=" ")
            num -= 1
        else:
            print("-", end=" ")
    print()