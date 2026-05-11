# 5.Number Stability Analyzer

# A science lab studies whether digits are in increasing order.

# Write a program using for-else loop:

# - If every next digit is greater than previous print Stable Number
# - Else Unstable Number

# Input:
# 12359

# Output:
# Stable Number

num_str = input()

for i in range(len(num_str) - 1):
    if int(num_str[i]) >= int(num_str[i+1]):
        print("Unstable Number")
        break
else:  # Executes only if no break occurs
    print("Stable Number")




#
# num_str = input()

# i = 0
# stable = True

# while i < len(num_str) - 1:
#     if int(num_str[i]) >= int(num_str[i + 1]):
#         print("Unstable Number")
#         stable = False
#         break
#     i += 1

# if stable:
#     print("Stable Number")