# 9. Student Attendance Eligibility System

# A college determines whether a student is eligible to sit for exams based on attendance percentage:

# * 75% and above → Eligible
# * 60% to 74% → Eligible with warning
# * Below 60% → Not eligible

# Write a Python program to check eligibility.

# Input:
# Enter attendance percentage: 58

# Output:
# Status: Not Eligible

attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    status = "Eligible"
elif attendance >= 60:
    status = "Eligible with Warning"
else:
    status = "Not Eligible"

print("Status:", status)