# 7.
#  Prime Sum Lucky Number

# A lottery app checks if sum of digits is prime.

# Write a program to:

# - Find sum of digits
# - If prime print Lucky Number
# - Else Normal Number

# Input:
# 4528

# Output:
# Sum = 19
# Lucky Number

n = int(input())

temp = n
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print("Sum =", digit_sum)

# Check if sum is prime
is_prime = True
if digit_sum <= 1: is_prime = False
else:
    i = 2
    while i * i <= digit_sum:
        if digit_sum % i == 0: is_prime = False; break
        i += 1

if is_prime:
    print("Lucky Number")
else:
    print("Normal Number")

#

# n = int(input())

# temp = n
# digit_sum = 0

# for _ in str(n):
#     digit_sum += temp % 10
#     temp //= 10

# print("Sum =", digit_sum)

# # Check if sum is prime
# is_prime = True
# if digit_sum <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(digit_sum**0.5) + 1):
#         if digit_sum % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Lucky Number")
# else:
#     print("Normal Number")