# 10.
# enter number6
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4



n = int(input("Enter number: "))

i = 1
while i <= n - 1:
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


