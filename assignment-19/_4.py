
# 4.Electricity Billing System
# An electricity board calculates bills based on units consumed:
# Up to 100 units → ₹5 per unit
# 101–300 units → ₹7 per unit
# Above 300 units → ₹10 per unit
# Write a program to compute total bill using inline if.


units = int(input("Enter units consumed: "))

bill = units * 5 if units <= 100 else 100 * 5 + (units - 100) * 7 if units <= 300 else 100 * 5 + 200 * 7 + (units - 300) * 10

print("Total Bill =", bill)