# 5.
# Tech Number Checker

# A number is called a Tech Number if:

# It has even number of digits
# Split it into two equal halves
# Add both halves
# Square the sum
# If result equals original number → Tech Number

# Write a program to:

# Count digits
# If digits are even, split the number
# Find sum of both halves
# Square the sum
# Display intermediate values
# Check and print result

# Input:
# 2025

# Output:
# First Half = 20
# Second Half = 25
# Sum = 45
# Square = 2025
# # Tech Number

num_str = input()
n = int(num_str)

# Count digits
digit_count = 0
for _ in num_str:
    digit_count += 1

if digit_count % 2 != 0:
    print("Not a Tech Number (Odd number of digits)")
else:
    mid = digit_count // 2
    
    # Extract halves using string slicing (clean & standard)
    first_half = int(num_str[:mid])
    second_half = int(num_str[mid:])
    
    total = first_half + second_half
    square = total * total
    
    print("First Half =", first_half)
    print("Second Half =", second_half)
    print("Sum =", total)
    print("Square =", square)
    
    if square == n:
        print("Tech Number")
    else:
        print("Not a Tech Number")


#
# num = input("Enter number: ")

# count = 0
# i = 0

# while i < len(num):
#     count += 1
#     i += 1

# if count % 2 != 0:
#     print("Not a Tech Number")
# else:
#     mid = count // 2

#     first_half_str = ""
#     second_half_str = ""

#     i = 0
#     while i < mid:
#         first_half_str += num[i]
#         i += 1

#     while i < count:
#         second_half_str += num[i]
#         i += 1

#     first_half = int(first_half_str)
#     second_half = int(second_half_str)

#     total = first_half + second_half
#     square = total * total

#     print("First Half =", first_half)
#     print("Second Half =", second_half)
#     print("Sum =", total)
#     print("Square =", square)

#     if square == int(num):
#         print("Tech Number")
#     else:
#         print("Not a Tech Number")