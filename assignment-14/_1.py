# 1. Triple Operation Prime Verification System

# A cybersecurity company generates a security score from entered access code.

# Write a program to:

# - Find sum of digits of the number
# - Reverse the number
# - Find absolute difference between original number and reverse
# - Add digit sum and difference
# - Check whether final result is Prime or Not Prime

# Input:
# 4215

# Output:
# Sum of Digits = 12
# Reverse = 5124
# Difference = 909
# Final Result = 921
# Not Prime

n = int(input())

# Sum of digits
temp = n
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print("Sum of Digits =", digit_sum)

# Reverse number
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse =", rev)

# Absolute difference
diff = abs(n - rev)
print("Difference =", diff)

# Final result
final = digit_sum + diff
print("Final Result =", final)

# Prime check
is_prime = True
if final <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= final:
        if final % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")


#

# n = int(input())

# # Sum of digits
# temp = n
# digit_sum = 0
# for _ in str(n):
#     digit_sum += temp % 10
#     temp //= 10
# print("Sum of Digits =", digit_sum)

# # Reverse number
# temp = n
# rev = 0
# for _ in str(n):
#     rev = rev * 10 + temp % 10
#     temp //= 10
# print("Reverse =", rev)

# # Absolute difference
# diff = abs(n - rev)
# print("Difference =", diff)

# # Final result
# final = digit_sum + diff
# print("Final Result =", final)

# # Prime check
# is_prime = True
# if final <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(final ** 0.5) + 1):
#         if final % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")
















