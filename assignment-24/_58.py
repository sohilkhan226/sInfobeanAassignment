# X 
# X X 
# X   X 
# X     X 
# X X X X X 

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()