# 1. Largest Digit in Number
# A cybersecurity company checks numeric passwords used in smart lockers.
# To identify password strength, the system finds the highest digit present in the entered password.
# Higher digits indicate stronger variation in the password pattern.
# Write a program to find the largest digit in a number using loops.

# Input:
# 57294

# Output:
# Largest Digit = 9

n=5724
largest=0
while n>0:
    r=n%10
    if largest<r:
        largest=r
    n//=10
print(largest)
    















# num = int(input("Enter number: "))
# largest = 0

# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num = num // 10

# print("Largest Digit =", largest)


#

# num = int(input("Enter number: "))
# temp = num
# largest = 0

# for _ in str(num):
#     digit = temp % 10
#     if digit > largest:
#         largest = digit
#     temp = temp // 10

# print("Largest Digit =", largest)
























