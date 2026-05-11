# 3.

# Fibonacci Population Growth Tracker

# A wildlife research team is studying the growth of a rare species.  
# They observe that the population follows a Fibonacci pattern:

# - Month 1 → 0 animals  
# - Month 2 → 1 animal  
# - Every next month → sum of previous two months  

# The researchers want to analyze the growth pattern.

# Write a program to:

# - Read number of months n
# - Generate Fibonacci series up to n months using loop
# - Print population for each month
# - Find total population observed
# - Count how many months population exceeded 5

# Input:
# 8

# Output:
# Population Growth:
# 0 1 1 2 3 5 8 13

# Total Population = 33
# Months with Population > 5 = 2

n = int(input())

a, b = 0, 1
total_pop = 0
months_gt_5 = 0

print("Population Growth:")
for _ in range(n):
    print(a, end=" ")
    total_pop += a
    if a > 5:
        months_gt_5 += 1
    a, b = b, a + b

print(f"\n\nTotal Population = {total_pop}")
print(f"Months with Population > 5 = {months_gt_5}")



#
# n = int(input())

# a, b = 0, 1
# total_pop = 0
# months_gt_5 = 0
# count = 0

# print("Population Growth:")

# while count < n:
#     print(a, end=" ")
#     total_pop += a
#     if a > 5:
#         months_gt_5 += 1
#     a, b = b, a + b
#     count += 1

# print()
# print()
# print("Total Population =", total_pop)
# print("Months with Population > 5 =", months_gt_5)