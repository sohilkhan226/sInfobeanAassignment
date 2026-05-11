# 5. Next Prime ID Generator – Smart Version

# A company gives prime numbered employee IDs to premium staff.

# Manager enters current ID.
# System must:

# - Find next prime number after current ID
# - Find difference between current ID and next prime

# Write a program using loops.

# Input:
# 20

# Output:
# Next Prime ID = 23
# Gap = 3

n = int(input())

cand = n + 1
while True:
    is_p = True
    if cand <= 1: is_p = False
    else:
        i = 2
        while i * i <= cand:
            if cand % i == 0: is_p = False; break
            i += 1
    if is_p:
        print("Next Prime ID =", cand)
        print("Gap =", cand - n)
        break
    cand += 1

#

# n = int(input())

# cand = n + 1
# found = False

# while not found:
#     is_p = True
#     if cand <= 1:
#         is_p = False
#     else:
#         for i in range(2, int(cand**0.5) + 1):
#             if cand % i == 0:
#                 is_p = False
#                 break
#     if is_p:
#         print("Next Prime ID =", cand)
#         print("Gap =", cand - n)
#         found = True
#     cand += 1