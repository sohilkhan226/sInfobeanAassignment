# 4. Prime Security Code Checker – Advanced

# A high-security lab accepts only prime numbered access codes.

# When a user enters a number, the software must:

# - Check whether number is prime
# - If prime, print next immediate prime number
# - If not prime, print previous immediate prime number

# Write a program using loops only.

# Input:
# 29

# Output:
# Prime Number
# Next Prime = 31

n = int(input())

# Check if n is prime
is_prime = True
if n <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print("Prime Number")
    # Find next prime
    cand = n + 1
    while True:
        p = True
        if cand <= 1: p = False
        else:
            j = 2
            while j * j <= cand:
                if cand % j == 0: p = False; break
                j += 1
        if p:
            print("Next Prime =", cand)
            break
        cand += 1
else:
    print("Not Prime Number")
    # Find previous prime
    cand = n - 1
    found = False
    while cand >= 2:
        p = True
        j = 2
        while j * j <= cand:
            if cand % j == 0: p = False; break
            j += 1
        if p:
            print("Previous Prime =", cand)
            found = True
            break
        cand -= 1
    if not found:
        print("No Previous Prime")


#
# n = int(input())

# # Check if n is prime
# is_prime = True
# if n <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime Number")
#     # Find next prime
#     cand = n + 1
#     found = False
#     while not found:
#         p = True
#         if cand <= 1:
#             p = False
#         else:
#             for j in range(2, int(cand**0.5) + 1):
#                 if cand % j == 0:
#                     p = False
#                     break
#         if p:
#             print("Next Prime =", cand)
#             found = True
#         cand += 1
# else:
#     print("Not Prime Number")
#     # Find previous prime
#     cand = n - 1
#     found = False
#     while cand >= 2 and not found:
#         p = True
#         for j in range(2, int(cand**0.5) + 1):
#             if cand % j == 0:
#                 p = False
#                 break
#         if p:
#             print("Previous Prime =", cand)
#             found = True
#         cand -= 1
#     if not found:
#         print("No Previous Prime")