# 9.Even Odd Difference Prime System

# A smart scanner counts even and odd digits.

# Write a program to:

# - Count even digits
# - Count odd digits
# - Find difference
# - Check whether difference is Prime or Not

# Input:
# 123456

# Output:
# Even Count = 3
# Odd Count = 3
# Difference = 0
# Not Prime


n = int(input())

temp = n
even_count = 0
odd_count = 0
while temp > 0:
    d = temp % 10
    if d % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    temp //= 10

diff = abs(even_count - odd_count)
print("Even Count =", even_count)
print("Odd Count =", odd_count)
print("Difference =", diff)

# Check if difference is prime
is_prime = True
if diff <= 1: is_prime = False
else:
    i = 2
    while i * i <= diff:
        if diff % i == 0: is_prime = False; break
        i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")


#
# n = int(input())

# temp = n
# even_count = 0
# odd_count = 0

# for _ in str(n):
#     d = temp % 10
#     if d % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     temp //= 10

# diff = abs(even_count - odd_count)
# print("Even Count =", even_count)
# print("Odd Count =", odd_count)
# print("Difference =", diff)

# # Check if difference is prime
# is_prime = True
# if diff <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(diff**0.5) + 1):
#         if diff % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")