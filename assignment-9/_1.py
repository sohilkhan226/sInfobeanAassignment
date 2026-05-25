# 1. Smart Credit Card Approval System

# A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

# If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt.
#  If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. 
#  If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

# If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

# Input:
# Income = 45000
# Credit Score = 720
# Employment = private
# Debt = 10000

# Output:
# Card Type = Silver Card

income        = int(input("Enter income: "))
credit_score  = int(input("Enter credit score: "))
employment    = input("Enter employment type: ").lower()
debt          = int(input("Enter existing debt: "))

if income >= 50000:
    if credit_score >= 750:
        if debt < 20000:
            card = "Premium Card"
        else:
            card = "Gold Card"
    else:
        if employment == "government" and credit_score >= 650:
            card = "Gold Card"
        else:
            card = "Rejected"
else:
    if income >= 30000 and credit_score >= 700:
        card = "Silver Card"
    else:
        card = "Rejected"

print("Card Type =", card)



















