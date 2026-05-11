# 3.
# Zero Detection & Early Termination System

# A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

# Write a program to:

# Traverse each digit of the number from right to left
# Display each digit processed before encountering 0
# Stop the loop immediately when 0 is found using break
# Count how many digits were processed before termination
# If no zero is found, print No Zero Found

# Use loops and break wherever required.

# Input:
# 572049

# Output:
# Digits Processed: 9 4
# Count = 2
# Zero Found - Process Stopped

# Input:
# 56789

# Output:
# Digits Processed: 9 8 7 6 5
# Count = 5
# No Zero Found

n_str = input()

count = 0
zero_found = False
print("Digits Processed:", end=" ")

# Traverse from right to left
i = len(n_str) - 1
while i >= 0:
    d = int(n_str[i])
    if d == 0:
        zero_found = True
        break
    print(d, end=" ")
    count += 1
    i -= 1
print()

print("Count =", count)
if zero_found:
    print("Zero Found - Process Stopped")
else:
    print("No Zero Found")


#
# n_str = input()

# count = 0
# zero_found = False
# print("Digits Processed:", end=" ")

# # Traverse from right to left using for loop
# for i in range(len(n_str) - 1, -1, -1):
#     d = int(n_str[i])
#     if d == 0:
#         zero_found = True
#         break
#     print(d, end=" ")
#     count += 1

# print()
# print("Count =", count)

# if zero_found:
#     print("Zero Found - Process Stopped")
# else:
#     print("No Zero Found")

