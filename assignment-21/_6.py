# 6.
# Palindrome Number Range Checker

# A barcode verification system checks for palindrome numbers within a specific range.
# The user enters starting and ending numbers.
# The system displays all palindrome numbers using nested loops.

# Input:
# Enter starting number: 100
# Enter ending number: 200

# Output:
# Palindrome Numbers are:
# 101
# 111
# 121
# 131
# 141
# 151
# 161
# 171
# 181
# 191


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome Numbers are:")

for num in range(start, end + 1):
    temp = num
    rev = 0

    for _ in str(num):
        rev = rev * 10 + temp % 10
        temp //= 10

    if rev == num:
        print(num)



