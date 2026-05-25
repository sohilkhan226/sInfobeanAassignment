# **8. Count Odd Digits**
# A banking system flags IDs with too many odd digits for further verification.
# Write a program to **count the number of odd digits in a given number using loops**.

# Input: 123456
# Output: Odd digits count = 3

# ---








number = int(input("Enter a number: "))

original   = number
odd_count  = 0

while original > 0:
    digit = original % 10
    if digit % 2 != 0:
        odd_count = odd_count + 1
    original = original // 10

print("Odd digits count =", odd_count)


#
# num = int(input("Enter a number: "))

# odd_count = 0
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     if digit % 2 != 0:
#         odd_count += 1
#     temp //= 10

# print("Odd digits count =", odd_count)