     1
    101
   10101
  1010101
 101010101
10101010101


n = 6
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()