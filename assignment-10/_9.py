# **9. Check All Digits Are Even**
# A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
# Write a program to **check whether all digits of a number are even using loops**.

# Input: 2468
# Output: All Even

# Input: 2456
# Output: Not All Even

# ---

number = int(input("Enter a number: "))

original  = number
all_even  = True

while original > 0:
    digit = original % 10
    if digit % 2 != 0:
        all_even = False
    original = original // 10

if all_even:
    print("All Even")
else:
    print("Not All Even")

#
# num = int(input("Enter a number: "))

# all_even = True
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     if digit % 2 != 0:
#         all_even = False
#         break
#     temp //= 10

# if all_even:
#     print("All Even")
# else:
#     print("Not All Even")