#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1


n = 5
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid:
            print(j + 1, end="")
        elif j == mid:
            print(i + 1, end="")
        else:
            print(" ", end="")
    print()