# 5.

# Automorphic Number Lock

# A high-security digital locker validates access codes using a special mathematical rule.

# When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
#  If it matches, the code is considered valid.

# An Automorphic Number is a number whose square ends with the same number.

# Task:
# Write a Python program to check whether a given number is an Automorphic Number or not.

# Example:
# Input:
# 25

# Output:
# Automorphic Number



n = int(input())

square = n * n
temp_n = n
temp_sq = square
is_automorphic = True

while temp_n > 0:
    if temp_n % 10 != temp_sq % 10:
        is_automorphic = False
        break
    temp_n //= 10
    temp_sq //= 10

if is_automorphic:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

#


# n = int(input())

# square = n * n
# temp_n = n
# temp_sq = square
# is_automorphic = True

# for _ in str(n):
#     if temp_n % 10 != temp_sq % 10:
#         is_automorphic = False
#         break
#     temp_n //= 10
#     temp_sq //= 10

# if is_automorphic:
#     print("Automorphic Number")
# else:
#     print("Not an Automorphic Number")