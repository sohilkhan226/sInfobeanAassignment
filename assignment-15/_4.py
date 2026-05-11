# 4.Spy Number Detector

# A cybersecurity system flags special numeric codes.

# A number is called a Spy Number if:
# Sum of digits = Product of digits

# Write a program to check whether the entered number is Spy Number or Not.

# Input:
# 1124

# Output:
# Spy Number

n = int(input())

temp = n
digit_sum = 0
digit_prod = 1

while temp > 0:
    d = temp % 10
    digit_sum += d
    digit_prod *= d
    temp //= 10

if digit_sum == digit_prod:
    print("Spy Number")
else:
    print("Not a Spy Number")

#
# n = int(input())

# digit_sum = 0
# digit_prod = 1

# for _ in str(n):
#     digit = n % 10
#     digit_sum += digit
#     digit_prod *= digit
#     n //= 10

# if digit_sum == digit_prod:
#     print("Spy Number")
# else:
#     print("Not a Spy Number")