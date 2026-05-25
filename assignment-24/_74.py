# x
# xx
# xxx
# xxxx
# xxx
# xx
# x

n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("x", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("x", end="")
    print()