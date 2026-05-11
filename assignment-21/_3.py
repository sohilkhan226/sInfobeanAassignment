# 3.
# Prime Number Range Checker

# A cyber security system generates prime numbers for encryption analysis.
# The user enters a starting number and ending number.
# The system checks and displays all prime numbers between the given range using nested loops.

# Input:
# Enter starting number: 10
# Enter ending number: 50

# Output:
# Prime Numbers are:
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime Numbers are:")

for num in range(start, end + 1):
    if num <= 1:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)