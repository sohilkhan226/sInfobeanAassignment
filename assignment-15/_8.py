# 8.
# Trimorphic Number Analyzer

# A coding system checks cube-based patterns.

# A Trimorphic Number:
# Cube of number ends with the same number.

# Example:
# 4³ = 64

# Write a program to check Trimorphic Number.

# Input:
# 4

# Output:
# Trimorphic Number

n = int(input())

cube = n ** 3
temp_n = n
temp_c = cube
is_trimorphic = True

while temp_n > 0:
    if temp_n % 10 != temp_c % 10:
        is_trimorphic = False
        break
    temp_n //= 10
    temp_c //= 10

if is_trimorphic:
    print("Trimorphic Number")
else:
    print("Not a Trimorphic Number")


#

# n = int(input())

# cube = n ** 3
# temp_n = n
# temp_c = cube
# is_trimorphic = True

# for _ in str(n):
#     if temp_n % 10 != temp_c % 10:
#         is_trimorphic = False
#         break
#     temp_n //= 10
#     temp_c //= 10

# if is_trimorphic:
#     print("Trimorphic Number")
# else:
#     print("Not a Trimorphic Number")