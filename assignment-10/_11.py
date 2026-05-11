
# **11. Count Occurrence of a Digit**
# A system logs repeated digits in a number for pattern analysis and reporting.
# Write a program to **count how many times a given digit appears in a number using loops**.

# Input: Number = 122312, Digit = 2
# Output: 3

# ---

number = int(input("Enter a number: "))
target = int(input("Enter digit to search: "))

original = number
count    = 0

while original > 0:
    digit = original % 10
    if digit == target:
        count = count + 1
    original = original // 10

print(count)

#
# num = int(input("Enter a number: "))
# target = int(input("Enter digit to search: "))

# count = 0
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     if digit == target:
#         count += 1
#     temp //= 10

# print(count)