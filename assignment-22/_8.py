# 8.
# enter n6
#  654321
#   65432
#    6543
#     654
#      65



n = int(input("Enter n: "))

i = 1
while i <= n:
    # Spaces
    j = 1
    while j < i:
        print(" ", end="")
        j += 1
    # Numbers from n down to i
    k = n
    while k >= i:
        print(k, end="")
        k -= 1
    print()
    i += 1