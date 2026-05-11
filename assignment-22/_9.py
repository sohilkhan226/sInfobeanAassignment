
# 9.
#     1
#    10
#   101
#  1010
# 10101


n = 5
i = 1

while i <= n:
    # Spaces
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    # Alternating 1 and 0
    k = 0
    while k < i:
        if k % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
        k += 1
    print()
    i += 1