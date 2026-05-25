# **12. Multiplication of Digits**
# A puzzle game calculates a score by multiplying all digits of a number together.
# After calculating the score, the game also checks whether
# the final score is even or odd to assign a bonus.
# Write a program to **find the product of all digits of a number using
# loops and then check whether the result is even or odd**.

# Input: 1234
# Output: 24
# Even

# ---

number = int(input("Enter a number: "))

original = number
product  = 1

while original > 0:
    digit    = original % 10
    product  = product * digit
    original = original // 10

print(product)

if product % 2 == 0:
    print("Even")
else:
    print("Odd")

#

# num = int(input("Enter a number: "))

# prod = 1
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     prod *= digit
#     temp //= 10

# print(prod)
# if prod % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
