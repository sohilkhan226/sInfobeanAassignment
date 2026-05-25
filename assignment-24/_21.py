# A
# AB
# A C
# A  D
# ABCDE


n = 5
for i in range(1, n + 1):
    for j in range(i):
        if i == n or j == 0 or j == i - 1:
            print(chr(65 + j), end="")
        else:
            print(" ", end="")
    print()