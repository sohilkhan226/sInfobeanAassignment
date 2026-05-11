# 7.
# Adam Number Verification System – Question

# A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

# When a user enters a numeric code, the system performs a dual verification process:

# * It calculates the square of the entered number.
# * It reverses the number and calculates the square of the reversed value.
# * Finally, it checks whether both results are mirror images (reverses) of each other.

# A number is called an Adam Number if:
# The square of the number and the square of its reverse are reverses of each other.

# Task:
# Write a Python program to check whether a given number is an Adam Number or not.

# Examples:

# Input:
# 12
# Output:
# Adam Number

# Input:
# 13
# Output:
# Not an Adam Number

# Input:
# 11
# Output:
# Adam Number

# Example:
# 12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144

def reverse_num(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = int(input())

sq_n = n * n
rev_n = reverse_num(n)
sq_rev_n = rev_n * rev_n
rev_sq_n = reverse_num(sq_n)

if rev_sq_n == sq_rev_n:
    print("Adam Number")
else:
    print("Not an Adam Number")


#

# def reverse_num(num):
#     rev = 0
#     for _ in str(num):
#         rev = rev * 10 + num % 10
#         num //= 10
#     return rev

# n = int(input())

# sq_n = n * n
# rev_n = reverse_num(n)
# sq_rev_n = rev_n * rev_n
# rev_sq_n = reverse_num(sq_n)

# if rev_sq_n == sq_rev_n:
#     print("Adam Number")
# else:
#     print("Not an Adam Number")


