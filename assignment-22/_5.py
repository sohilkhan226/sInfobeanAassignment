# 5)
# A
# AB
# ABC
# ABCD
# ABCDE

n = 5
i = 1

while i <= n:
    j = 0
    while j < i:
        print(chr(65 + j), end="")
        j += 1
    print()
    i += 1