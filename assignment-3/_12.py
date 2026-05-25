
# Assignment 12: Change Return System

# Write a Python program that:

# Accepts amount.
# Calculates ₹100, ₹50, ₹10 notes.

# Input:
# Amount = 380

# Output:
# ₹100 x 3
# ₹50 x 1
# ₹10 x 3


amount = 380

note100= amount//100
amount = amount%100

note50 =amount//50
amount=amount%50

note10 = amount//10

print(f"₹100 x {note100}\n₹50 x {note50}\n₹10 x {note10}")














