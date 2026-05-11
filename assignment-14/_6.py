# 6.
# Next Prime Cabin Number Generator

# A luxury hotel gives only prime numbered cabins to VIP guests.

# Manager enters the last allotted cabin number.
# System must find the next available prime cabin number.

# Write a program using loops.

# Input:
# 24

# Output:
# Next Prime Cabin = 29

n = int(input())
cand = n + 1

while True:
    is_prime = True
    if cand <= 1:
        is_prime = False
    else:
        i = 2
        while i * i <= cand:
            if cand % i == 0:
                is_prime = False
                break
            i += 1
            
    if is_prime:
        print("Next Prime Cabin =", cand)
        break
    cand += 1


#


# n = int(input())

# for cand in range(n + 1, 10**9):
#     is_prime = True

#     if cand <= 1:
#         is_prime = False
#     else:
#         for i in range(2, int(cand ** 0.5) + 1):
#             if cand % i == 0:
#                 is_prime = False
#                 break

#     if is_prime:
#         print("Next Prime Cabin =", cand)
#         break