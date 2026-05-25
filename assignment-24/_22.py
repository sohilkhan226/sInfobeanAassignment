# a
# bc
# d f
# g  j
# klmno


ch = 97
n = 5
for i in range(1, n + 1):
    for j in range(i):
        if i == n or j == 0 or j == i - 1:
            print(chr(ch), end="")
        else:
            print(" ", end="")
        ch += 1
    print()