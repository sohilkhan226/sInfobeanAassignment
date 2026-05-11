# 8. Largest Smallest Sum Prime Checker

# A number analyzer finds largest and smallest digit.

# Write a program to:

# - Find largest digit
# - Find smallest digit
# - Find sum of both
# - Check whether sum is Prime or Not

# Input:
# 57294

# Output:
# Largest = 9
# Smallest = 2
# Sum = 11
# Prime

n = int(input())

temp = n
largest = -1
smallest = 10
while temp > 0:
    d = temp % 10
    if d > largest: largest = d
    if d < smallest: smallest = d
    temp //= 10

s = largest + smallest
print("Largest =", largest)
print("Smallest =", smallest)
print("Sum =", s)

# Check if sum is prime
is_prime = True
if s <= 1: is_prime = False
else:
    i = 2
    while i * i <= s:
        if s % i == 0: is_prime = False; break
        i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")

#

# n = int(input())

# temp = n
# largest = -1
# smallest = 10

# for _ in str(n):
#     d = temp % 10
#     if d > largest:
#         largest = d
#     if d < smallest:
#         smallest = d
#     temp //= 10

# s = largest + smallest
# print("Largest =", largest)
# print("Smallest =", smallest)
# print("Sum =", s)

# # Check if sum is prime
# is_prime = True
# if s <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(s**0.5) + 1):
#         if s % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")