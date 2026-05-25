# ABCDE
# A__D
# A_C
# AB
# A

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        if i == n or j == 0 or j == i - 1:
            print(chr(65 + j), end="")
        else:
            print("_", end="")
    print()