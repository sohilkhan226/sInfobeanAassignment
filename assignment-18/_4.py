# 4.Digit Gap Analyzer

# A system analyzes the gap between consecutive digits.

# Write a program to:

# Traverse digits from left to right
# Find the absolute difference between current digit and next digit
# Display each difference
# Count how many differences are greater than 2
# Find the maximum difference
# If all differences ≤ 2 → print Smooth Number
# Else → print Irregular Pattern

# Input:
# 86421

# Output:
# Differences: 2 2 2 1
# Count (>2) = 0
# Max Difference = 2
# Smooth Number


num_str = input()

digits = []
for ch in num_str:
    digits.append(int(ch))

diffs = []
for i in range(len(digits) - 1):
    diffs.append(abs(digits[i] - digits[i+1]))

print("Differences:", end=" ")
for d in diffs:
    print(d, end=" ")
print()

count_gt2 = 0
for d in diffs:
    if d > 2:
        count_gt2 += 1
print("Count (>2) =", count_gt2)

max_diff = diffs[0]
for d in diffs:
    if d > max_diff:
        max_diff = d
print("Max Difference =", max_diff)

if count_gt2 == 0:
    print("Smooth Number")
else:
    print("Irregular Pattern")

#
# num = input("Enter number: ")

# i = 0
# count_gt_2 = 0
# max_diff = 0

# print("Differences:", end=" ")

# while i < len(num) - 1:
#     d1 = int(num[i])
#     d2 = int(num[i + 1])

#     if d1 > d2:
#         diff = d1 - d2
#     else:
#         diff = d2 - d1

#     print(diff, end=" ")

#     if diff > 2:
#         count_gt_2 += 1

#     if i == 0 or diff > max_diff:
#         max_diff = diff

#     i += 1

# print()
# print("Count (>2) =", count_gt_2)
# print("Max Difference =", max_diff)

# if count_gt_2 == 0:
#     print("Smooth Number")
# else:
#     print("Irregular Pattern")