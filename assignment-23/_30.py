# 30) Extended Slanted Star Block
#     ****
#      ****
#       ****
#        ****
#         ****


n = 5
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(4):
        print("*", end="")
    print()