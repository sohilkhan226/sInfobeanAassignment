# Assignment 2: Mobile EMI Calculation

# You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

# Input:
# Mobile price = 30000
# Down payment = 5000
# Interest rate = 10%
# Months = 10

# Expected Output:
# Remaining Amount = 25000
# Total with Interest = 27500
# Monthly EMI = 2750.0

price = float(input("Enter mobile price: "))
down_payment = float(input("Enter down payment: "))
interest_rate = float(input("Enter interest rate: "))
months = int(input("Enter number of months: "))

remaining_amount = price - down_payment
interest = remaining_amount * interest_rate / 100
total_with_interest = remaining_amount + interest
emi = total_with_interest / months

print("Remaining Amount =", remaining_amount)
print("Total with Interest =", total_with_interest)
print("Monthly EMI =", emi)