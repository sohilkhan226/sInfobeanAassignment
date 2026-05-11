# 2. Digit Sum Mirror Checker

# A validation system checks symmetry in digit sums.

# Write a program to:

# Split number into two halves
# Find sum of first half digits
# Find sum of second half digits
# Display both sums
# If both sums are equal → print Balanced Number
# Else → print Unbalanced Number

# Input:
# 123321

# Output:
# First Half Sum = 6
# Second Half Sum = 6
# Balanced Number

num_str = input()

digits = []
for ch in num_str:
    digits.append(int(ch))

mid = len(digits) // 2

# Sum of first half
first_half_sum = 0
for i in range(mid):
    first_half_sum += digits[i]

# Sum of second half
second_half_sum = 0
for i in range(mid, len(digits)):
    second_half_sum += digits[i]

print("First Half Sum =", first_half_sum)
print("Second Half Sum =", second_half_sum)

if first_half_sum == second_half_sum:
    print("Balanced Number")
else:
    print("Unbalanced Number")

#
# num = input("Enter number: ")

# length = len(num)
# mid = length // 2

# first_half_sum = 0
# second_half_sum = 0

# i = 0
# while i < mid:
#     first_half_sum += int(num[i])
#     i += 1

# while i < length:
#     second_half_sum += int(num[i])
#     i += 1

# print("First Half Sum =", first_half_sum)
# print("Second Half Sum =", second_half_sum)

# if first_half_sum == second_half_sum:
#     print("Balanced Number")
# else:
#     print("Unbalanced Number")

