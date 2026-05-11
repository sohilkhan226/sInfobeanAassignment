# 7. Power of a Number
# A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
# Write a program to calculate n raised to power p using loops.

# Input:
# 2 5

# Output:
# 32

n = int(input("Enter base: "))
p = int(input("Enter power: "))
result = 1

for i in range(p):
    result *= n

print(result)

#

# n = int(input("Enter base: "))
# p = int(input("Enter power: "))
# result = 1
# i = 0

# while i < p:
#     result *= n
#     i += 1

# print(result)