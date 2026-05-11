# 5. Palindrome Check
# A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
# Write a program to **check whether a given number is a palindrome using loops**.

# Input: 121
# Output: Palindrome

# ---

number = int(input("Enter a number: "))

original        = number
reversed_number = 0

while original > 0:
    last_digit      = original % 10
    reversed_number = reversed_number * 10 + last_digit
    original        = original // 10

if number == reversed_number:
    print("Palindrome")
else:
    print("Not a Palindrome")

#
# num = int(input("Enter a number: "))

# rev = 0
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10

# if num == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")