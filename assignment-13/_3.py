# 3. Composite Number Detector

# A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

# The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

# Write a program to check whether a number is Composite or Not.

# Input:
# 12

# Output:
# Composite Number

n = int(input())

if n <= 1:
    print("Not Composite Number")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
        
    if not is_prime:
        print("Composite Number")
    else:
        print("Not Composite Number")

#

# n = int(input())

# if n <= 1:
#     print("Not Composite Number")
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

#     if not is_prime:
#         print("Composite Number")
#     else:
#         print("Not Composite Number")