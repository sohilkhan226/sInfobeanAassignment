# 4. Reverse a Number
# A security system stores OTP codes in reverse format for
#encryption to increase data safety. Reversing a number means extracting 
#digits and rebuilding it in reverse order.
# Write a program to **reverse a given integer using loops**.

# Input: 1234
# Output: 4321

# ---

num = int(input("Enter a number: "))

rev = 0
temp = num
# for loop runs exactly number-of-digits times
for _ in str(num):         '''1234 => 1 => 2 => 3 => 4 =>    string me 1,1 karke leta h'''
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print(rev)