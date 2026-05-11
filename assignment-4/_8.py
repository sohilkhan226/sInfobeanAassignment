# Assignment 8: Compound Interest

# A person invests money in a bank that provides compound interest annually.

# Input:
# Principal = 10000
# Rate = 5%
# Time = 2 years

# Expected Output:
# Amount after interest = 11025.0

principal = 10000
rate = 5
time = 2

amount = principal * (1 + rate / 100) ** time

print("Amount after interest =", amount)