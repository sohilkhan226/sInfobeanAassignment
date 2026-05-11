# 10.Zero Count Prime Scanner

# A banking system checks account numbers.

# Write a program to:

# - Count zero digits
# - Find sum of digits
# - Add zero count and sum
# - Multiply by smallest digit
# - Check whether final result is Prime or Not

# Input:
# 908406

# Output:
# Zero Count = 2
# Sum = 27
# Smallest Digit = 0
# Final Result = 0
# Not Prime

n = int(input())

temp = n
zero_count = 0
digit_sum = 0
smallest = 10
while temp > 0:
    d = temp % 10
    if d == 0:
        zero_count += 1
    digit_sum += d
    if d < smallest:
        smallest = d
    temp //= 10

final_result = (zero_count + digit_sum) * smallest
print("Zero Count =", zero_count)
print("Sum =", digit_sum)
print("Smallest Digit =", smallest)
print("Final Result =", final_result)

# Check if final result is prime
is_prime = True
if final_result <= 1: is_prime = False
else:
    i = 2
    while i * i <= final_result:
        if final_result % i == 0: is_prime = False; break
        i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")

#

# n = int(input())

# temp = n
# zero_count = 0
# digit_sum = 0
# smallest = 10

# for _ in str(n):
#     d = temp % 10
#     if d == 0:
#         zero_count += 1
#     digit_sum += d
#     if d < smallest:
#         smallest = d
#     temp //= 10

# final_result = (zero_count + digit_sum) * smallest
# print("Zero Count =", zero_count)
# print("Sum =", digit_sum)
# print("Smallest Digit =", smallest)
# print("Final Result =", final_result)

# # Check if final result is prime
# is_prime = True
# if final_result <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(final_result**0.5) + 1):
#         if final_result % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")