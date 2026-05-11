# 4. Strong Number Checker

# A digital lock opens only for strong numbers.

# A strong number is a number whose sum of factorial of digits equals the number.

# Example:
# 145 = 1! + 4! + 5!

# Write a program using loops to check strong number.

# Input:
# 145

# Output:
# Strong Number

n = int(input())

temp = n
total = 0

while temp > 0:
    digit = temp % 10
    
    # Calculate factorial of digit using loop
    fact = 1
    j = 1
    while j <= digit:
        fact *= j
        j += 1
        
    total += fact
    temp //= 10

if total == n:
    print("Strong Number")
else:
    print("Not a Strong Number")


#

# n = int(input())

# temp = n
# total = 0

# for _ in str(n):
#     digit = temp % 10

#     # Inner for loop for factorial
#     fact = 1
#     for j in range(1, digit + 1):
#         fact *= j

#     total += fact
#     temp //= 10

# if total == n:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")