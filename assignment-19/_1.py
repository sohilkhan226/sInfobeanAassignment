# 1. Smart Shopping Mall Discount System
# A shopping mall offers discounts based on customer type and purchase amount.
# If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
# If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
# Write a program to calculate the final payable amount using inline if only.


customer = input("Enter customer type: ").lower()
amount = float(input("Enter purchase amount: "))

discount = (20 / 100 if amount > 5000 else 10 / 100) if customer == "premium" else (10 / 100 if amount > 3000 else 5 / 100)
final_amount = amount - amount * discount

print("Final Payable Amount =", final_amount)

