# Assignment 14: Simple Profit or Loss Calculator

# Write a Python program that:

# Accepts cost price and selling price.
# Calculates profit/loss and percentage.

# Input:
# Cost Price = 1000
# Selling Price = 1200

# Output:
# Profit = 200
# Profit % = 20.0

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

profit = sp - cp
profit_percent = (profit / cp) * 100

print("Profit =", profit)
print("Profit % =", profit_percent)