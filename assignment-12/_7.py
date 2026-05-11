# 7. Duck Number Checker

# A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

# A duck number is a number that contains at least one zero but does not start with zero.

# Example:
# 1023

# Write a program using loops to check whether the entered number is a Duck number.

# Input:
# 1023

# Output:
# Duck Number

num_str = input()

# Check if starts with zero
if num_str[0] == '0':
    print("Not a Duck Number")
else:
    has_zero = False
    i = 1
    while i < len(num_str):
        if num_str[i] == '0':
            has_zero = True
            break
        i += 1
        
    if has_zero:
        print("Duck Number")
    else:
        print("Not a Duck Number")

#

# num_str = input()

# if num_str[0] == '0':
#     print("Not a Duck Number")
# else:
#     has_zero = False

#     for i in range(1, len(num_str)):
#         if num_str[i] == '0':
#             has_zero = True
#             break

#     if has_zero:
#         print("Duck Number")
#     else:
#         print("Not a Duck Number")
