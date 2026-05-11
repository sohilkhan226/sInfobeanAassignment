# 9.
# Step Difference Number Analyzer

# A mathematics research center studies hidden patterns inside numbers.
# For every entered number, the system compares adjacent digits step by step.

# Write a program to:

# Find the absolute difference between every pair of adjacent digits
# Display all step differences
# Find the sum of all step differences
# Find the largest step difference
# If the sum of step differences is divisible by the number of digits, print Balanced Number
# Otherwise print Unbalanced Number

# Use loops wherever required.

# Input:
# 57294
# Output:
# Step Differences: 2 5 7 5
# Sum = 19
# Largest = 7
# Unbalanced Number

n = int(input())

# Extract digits using loop
temp = n
digits = []
while temp > 0:
    digits.append(temp % 10)
    temp //= 10
digits.reverse()  # Restore original order

# Calculate step differences
step_diffs = []
i = 0
while i < len(digits) - 1:
    diff = abs(digits[i] - digits[i+1])
    step_diffs.append(diff)
    i += 1

# Display step differences
print("Step Differences:", end=" ")
j = 0
while j < len(step_diffs):
    print(step_diffs[j], end=" ")
    j += 1
print()

# Calculate sum and largest difference
total = 0
largest = step_diffs[0]
k = 0
while k < len(step_diffs):
    total += step_diffs[k]
    if step_diffs[k] > largest:
        largest = step_diffs[k]
    k += 1

print("Sum =", total)
print("Largest =", largest)

# Check balanced condition
num_digits = len(digits)
if total % num_digits == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")

#

# n = int(input())

# # Extract digits using for loop
# temp = n
# digits = []
# for _ in str(n):
#     digits.append(temp % 10)
#     temp //= 10
# digits.reverse()

# # Calculate step differences
# step_diffs = []
# for i in range(len(digits) - 1):
#     diff = abs(digits[i] - digits[i + 1])
#     step_diffs.append(diff)

# # Display step differences
# print("Step Differences:", end=" ")
# for d in step_diffs:
#     print(d, end=" ")
# print()

# # Calculate sum and largest
# total = 0
# largest = step_diffs[0]
# for d in step_diffs:
#     total += d
#     if d > largest:
#         largest = d

# print("Sum =", total)
# print("Largest =", largest)

# # Check balanced condition
# num_digits = len(digits)
# if total % num_digits == 0:
#     print("Balanced Number")
# else:
#     print("Unbalanced Number")