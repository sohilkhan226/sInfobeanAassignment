# 3. First Digit of Number
# A university receives thousands of application IDs. 
# The first digit of each ID represents the department code, 
# so the admission software must read the first digit quickly.
# Write a program to find the first digit of a number using loops.

# Input:
# 53892

# Output:
# First Digit = 5

num = int(input("Enter number: "))

while num >= 10:
    num = num // 10

print("First Digit =", num)

#

# num = int(input("Enter number: "))
# temp = num

# for _ in range(len(str(num)) - 1):
#     temp = temp // 10

# print("First Digit =", temp)