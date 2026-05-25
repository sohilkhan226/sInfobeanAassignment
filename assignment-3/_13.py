
# Assignment 13: Compound Interest Calculator

# Write a Python program that:

# Accepts principal, rate, and time.
# Calculates compound interest.

# Input:
# Principal = 1000
# Rate = 10
# Time = 2

# Output:
# Amount = 1210.0
# Compound Interest = 210.0

rincipal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

amount = principal * (1 + rate / 100) ** time
ci = amount - principal

print("Amount =", amount)
print("Compound Interest =", ci)


# principal = int(input("enter the principal"))
# Rate      = int(input("enter the rate"))
# Time      = int(input("enter the Time"))

# amount = principal*(1+Rate/100)**Time

# print(f"amount={amount:.2f}")



