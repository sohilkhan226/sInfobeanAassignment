# 4.
# Armstrong Number Finder

# A digital number analysis system checks for Armstrong numbers within a range.
# The user enters starting and ending numbers.
# The system finds all Armstrong numbers using nested loops.

# Input:
# Enter starting number: 1
# Enter ending number: 500

# Output:
# Armstrong Numbers are:
# 1
# 153
# 370
# 371
# 407

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong Numbers are:")

for num in range(start, end + 1):
    temp = num
    arm_sum = 0
    digits = len(str(num))

    for _ in str(num):
        digit = temp % 10
        arm_sum += digit ** digits
        temp //= 10

    if arm_sum == num:
        print(num)

