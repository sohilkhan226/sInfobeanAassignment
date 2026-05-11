# 7.
# Neon Number Detector

# Scenario:
# A smart calculator system checks special numbers used in mathematical testing.
# The user enters a range of numbers.
# The system identifies all Neon Numbers using nested loops.

# Theory:
# A Neon Number is a number where the sum of digits of its square is equal to the original number.

# Example:
# 9

# Square of 9 = 81

# 8 + 1 = 9

# Since the sum is equal to the original number, 9 is called a Neon Number.

# Input:
# Enter starting number: 1
# Enter ending number: 100

# Output:
# Neon Numbers are:
# 1
# 9


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Neon Numbers are:")

for num in range(start, end + 1):
    square = num * num
    temp = square
    digit_sum = 0

    for _ in str(square):
        digit_sum += temp % 10
        temp //= 10

    if digit_sum == num:
        print(num)