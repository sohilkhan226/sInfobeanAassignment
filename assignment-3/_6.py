# Assignment 6: Discount Calculator

# Write a Python program that:

# Accepts total amount.
# Calculates 10% discount and final price.

# Input:
# Amount = 1000

# Output:
# Discount = 100
# Final = 900
# ------------------

  amount = float(input("Enter total amount: "))
  
  discount = amount * 10 // 100
  final = amount - discount
  
  print("Discount =", discount)
  print("Final =", final)