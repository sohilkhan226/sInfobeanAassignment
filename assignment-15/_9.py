# 9.
# Abundant Number Detector

# A financial system analyzes surplus numbers.

# An Abundant Number:
# Sum of proper factors > number

# Write a program to check Abundant Number.

# Input:
# 12

# Output:
# Abundant Number


n = int(input())

total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total > n:
    print("Abundant Number")
else:
    print("Not an Abundant Number")

#

# n = int(input())

# total = 0
# i = 1

# while i < n:
#     if n % i == 0:
#         total += i
#     i += 1

# if total > n:
#     print("Abundant Number")
# else:
#     print("Not an Abundant Number")