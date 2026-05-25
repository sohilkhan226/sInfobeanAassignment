# 8.
# Mirror Difference Transaction Verification System
# A multinational banking company processes thousands of daily transaction IDs.
# To detect suspicious patterns and validate system-generated IDs,
#  the security software performs a Mirror Difference Verification Test.
# For every entered transaction ID:

# Reverse the digits of the transaction ID

# Find the absolute difference between the original ID and the reversed ID


# Count the total number of digits in the difference
# Apply the following conditions using if-elif-else:

# If the difference is 0, print Perfect Match

# Else if the difference is divisible by 9, p rint Verified

# Else print Rejected


# Write a program to automate this verification process using loops and conditional statements.
# Input:
# 4215
# Output:
# Reverse = 5124Difference = 909Digits = 3Verified
# Input:
# 1221
# Output:
# Reverse = 1221Difference = 0Digits = 1Perfect Match
# Input:
# 1234
# Output:
# Reverse = 4321Difference = 3087Digits = 4Verified

n=int(input("enter the numeber"))
rev=""
for i in str(n):
    rev=i+rev
reverse = int(rev)
difference = reverse-n
length=len(str(difference))

if difference==0:
    status="perfect match"
elif difference%9==0:
    status="varified"
else:
    status="Rejected"

print(f"revrse={reverse} difference={difference} digits={length}variefid")










'''
n = int(input())

# Reverse the number
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse =", rev)

# Absolute difference
diff = abs(n - rev)
print("Difference =", diff)

# Count digits in difference
if diff == 0:
    digits = 1
else:
    temp_diff = diff
    digits = 0
    while temp_diff > 0:
        digits += 1
        temp_diff //= 10
print("Digits =", digits)

# Verification conditions
if diff == 0:
    print("Perfect Match")
elif diff % 9 == 0:
    print("Verified")
else:
    print("Rejected")


#
# n = int(input())

# # Reverse using for loop
# temp = n
# rev = 0
# for _ in str(n):
#     rev = rev * 10 + temp % 10
#     temp //= 10
# print("Reverse =", rev)

# # Absolute difference
# diff = abs(n - rev)
# print("Difference =", diff)

# # Count digits in difference
# if diff == 0:
#     digits = 1
# else:
#     temp_diff = diff
#     digits = 0
#     for _ in str(diff):
#         digits += 1
#         temp_diff //= 10
# print("Digits =", digits)

# # Verification conditions
# if diff == 0:
#     print("Perfect Match")
# elif diff % 9 == 0:
#     print("Verified")
# else:
#     print("Rejected")
'''