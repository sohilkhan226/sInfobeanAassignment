# 6. Armstrong Number (3-digit)
# In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
# Write a program to **check whether a number is an Armstrong number using loops**.

# Input: 153
# Output: Armstrong

# ---

number = int(input("Enter a 3-digit number: "))

original = number
arm_sum  = 0

while original > 0:
    digit   = original % 10
    arm_sum = arm_sum + digit ** 3
    original = original // 10

if arm_sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")

#
# num = int(input("Enter a 3-digit number: "))

# arm_sum = 0
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     arm_sum += digit ** 3
#     temp //= 10

# if arm_sum == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")