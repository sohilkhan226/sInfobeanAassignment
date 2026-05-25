# 1.Digit Product Analyzer System

# A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

# For every entered number, the system analyzes relationships between its digits.

# Write a program to:

# Find the product of every pair of adjacent digits
# Display all the products
# Find the sum of all these products
# Find the smallest product value
# If the sum of products is divisible by the total number of digits, print Stable Number
# Otherwise print Unstable Number

# Use loops wherever required.

# Input:
# 57294

# Output:
# Products: 35 14 18 36
# Sum = 103
# Smallest = 14
# Unstable Number
'''
n_str = input()

# Extract digits using loop
digits = []
for ch in n_str:
    digits.append(int(ch))

# Find products of adjacent digits
products = []
i = 0
while i < len(digits) - 1:
    products.append(digits[i] * digits[i+1])
    i += 1

# Display products
print("Products:", end=" ")
for p in products:
    print(p, end=" ")
print()

# Find sum and smallest product
total = 0
smallest = products[0]
for p in products:
    total += p
    if p < smallest:
        smallest = p

print("Sum =", total)
print("Smallest =", smallest)

# Check stability
if total % len(digits) == 0:
    print("Stable Number")
else:
    print("Unstable Number")
'''