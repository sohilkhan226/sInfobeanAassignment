# 7.
# enter n6
#      *
#     **
#    ***
#   ****
#  *****
# ******

n = int(input("Enter n: "))

i = 1
while i <= n:
    # Spaces
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    # Stars
    k = 1
    while k <= i:
        print("*", end="")
        k += 1
    print()
    i += 1