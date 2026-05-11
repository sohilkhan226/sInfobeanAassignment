# 1. Adjacent Digit Difference Analyzer

# A system analyzes differences between consecutive digits in a number.

# Write a program to:

# Find the difference between every pair of adjacent digits
# Display all differences
# Count how many differences are even
# Find the largest difference
# If all differences are same → print Uniform Difference
# Else → print Non-Uniform Pattern

# Input:
# 84261

# Output:
# Differences: 4 2 4 5
# Even Differences Count = 3
# Max Difference = 5
# Non-Uniform Pattern

num_str = input()

# Extract digits using loop
digits = []
for ch in num_str:
    digits.append(int(ch))

# Find absolute differences between adjacent digits
diffs = []
for i in range(len(digits) - 1):
    diffs.append(abs(digits[i] - digits[i+1]))

# Display differences
print("Differences:", end=" ")
for d in diffs:
    print(d, end=" ")
print()

# Count even differences
even_count = 0
for d in diffs:
    if d % 2 == 0:
        even_count += 1
print("Even Differences Count =", even_count)

# Find maximum difference
max_diff = diffs[0]
for d in diffs:
    if d > max_diff:
        max_diff = d
print("Max Difference =", max_diff)

# Check if all differences are same
is_uniform = True
for i in range(1, len(diffs)):
    if diffs[i] != diffs[0]:
        is_uniform = False
        break

if is_uniform:
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")


#
# num = input("Enter number: ")

# i = 0
# even_count = 0
# max_diff = 0
# uniform = True
# first_diff = -1

# print("Differences:", end=" ")

# while i < len(num) - 1:
#     d1 = int(num[i])
#     d2 = int(num[i + 1])

#     if d1 > d2:
#         diff = d1 - d2
#     else:
#         diff = d2 - d1

#     print(diff, end=" ")

#     if diff % 2 == 0:
#         even_count += 1

#     if i == 0:
#         first_diff = diff
#         max_diff = diff
#     else:
#         if diff != first_diff:
#             uniform = False
#         if diff > max_diff:
#             max_diff = diff

#     i += 1

# print()
# print("Even Differences Count =", even_count)
# print("Max Difference =", max_diff)

# if uniform:
#     print("Uniform Difference")
# else:
#     print("Non-Uniform Pattern")

