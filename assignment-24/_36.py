# *****
# ####
# ***
# ##
# *

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        if i % 2 != 0:
            print("*", end="")
        else:
            print("#", end="")
    print()