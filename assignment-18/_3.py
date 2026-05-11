# 3.
# Digit Neighbor Sum Analyzer

# A system analyzes the relationship between a digit and its immediate neighbors.

# Write a program to:

# Traverse digits from left to right (ignore first and last digit)
# For each digit, calculate sum of its adjacent digits
# Check if current digit is equal to the sum of its neighbors
# Display such digits
# Count how many such digits exist
# If none found → print No Matching Digit
# Else → print Neighbor Sum Pattern Found

# Input:
# 121314

# Output:
# Matching Digits: 2 3
# Count = 2
# Neighbor Sum Pattern Found


num_str = input()

digits = []
for ch in num_str:
    digits.append(int(ch))

matching = []
# Traverse ignoring first and last digit
for i in range(1, len(digits) - 1):
    neighbor_sum = digits[i-1] + digits[i+1]
    if digits[i] == neighbor_sum:
        matching.append(digits[i])

print("Matching Digits:", end=" ")
for m in matching:
    print(m, end=" ")
print()

print("Count =", len(matching))

if len(matching) == 0:
    print("No Matching Digit")
else:
    print("Neighbor Sum Pattern Found")

#
# num = input("Enter number: ")

# i = 1
# count = 0

# print("Matching Digits:", end=" ")

# while i < len(num) - 1:
#     left_digit = int(num[i - 1])
#     current_digit = int(num[i])
#     right_digit = int(num[i + 1])

#     if current_digit == left_digit + right_digit:
#         print(current_digit, end=" ")
#         count += 1

#     i += 1

# print()
# print("Count =", count)

# if count == 0:
#     print("No Matching Digit")
# else:
#     print("Neighbor Sum Pattern Found")