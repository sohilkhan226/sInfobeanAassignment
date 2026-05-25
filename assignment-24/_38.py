# 123456
# 54321
# 1234
# 321
# 12
# 1

n = 6
toggle = True
for i in range(1, n + 1):
    if toggle:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    toggle = not toggle
    print()