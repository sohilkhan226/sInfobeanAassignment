# 6. Banking Fraud Detection System

# A bank monitors transactions based on amount, location, OTP verification, and account age.

# If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

# Input:
# Transaction Amount = 60000
# Location = domestic
# Account Age = 1

# Output:
# Transaction Status = Flagged

transaction_amount = int(input("Enter transaction amount: "))
location = input("Enter location: ").lower()

if transaction_amount >= 10000:
    if location == "international":
        otp_status = input("Enter OTP status (verified/not verified): ").lower()
        if otp_status == "verified":
            status = "Allowed"
        else:
            status = "Blocked"
    else:
        if transaction_amount >= 50000:
            account_age = int(input("Enter account age: "))
            if account_age >= 2:
                status = "Allowed"
            else:
                status = "Flagged"
        else:
            status = "Allowed"
else:
    unusual_activity = input("Enter unusual activity (yes/no): ").lower()
    if unusual_activity == "yes":
        status = "Flagged"
    else:
        status = "Allowed"

print("Transaction Status =", status)