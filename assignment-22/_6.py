# 6)
# a
# ab
# abc
# abcd
# abcde


n = 5
i = 1

while i <= n:
    j = 0
    while j < i:
        print(chr(97 + j), end="")
        j += 1
    print()
    i += 1