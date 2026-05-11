# 2. Multi Stage Prime Lock System

# A smart locker opens only if final derived number is prime.

# Write a program to:

# - Find sum of digits
# - Find product of digits
# - Find difference between product and sum
# - Count digits in difference
# - Add digit count to difference
# - Check whether final result is Prime or Not

# Input:
# 234

# Output:
# Sum = 9
# Product = 24
# Difference = 15
# Digits = 2
# Final Result = 17
# Prime

n = int(input())

# Sum & Product of digits
temp = n
digit_sum = 0
digit_prod = 1
while temp > 0:
    d = temp % 10
    digit_sum += d
    digit_prod *= d
    temp //= 10
print("Sum =", digit_sum)
print("Product =", digit_prod)

# Difference
diff = digit_prod - digit_sum
print("Difference =", diff)

# Count digits in difference
temp_diff = abs(diff)
if temp_diff == 0:
    count = 1
else:
    count = 0
    while temp_diff > 0:
        count += 1
        temp_diff //= 10
print("Digits =", count)

# Final result
final = diff + count
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

# # Sum & Product of digits
# temp = n
# digit_sum = 0
# digit_prod = 1

# for _ in str(n):
#     d = temp % 10
#     digit_sum += d
#     digit_prod *= d
#     temp //= 10

# print("Sum =", digit_sum)
# print("Product =", digit_prod)

# # Difference
# diff = digit_prod - digit_sum
# print("Difference =", diff)

# # Count digits in difference
# temp_diff = abs(diff)
# if temp_diff == 0:
#     count = 1
# else:
#     count = 0
#     for _ in str(temp_diff):
#         count += 1

# print("Digits =", count)

# # Final result
# final = diff + count
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