# 10. Mobile Data Plan Advisor


# A telecom company suggests the most suitable data plan based on a user’s daily data usage:

# * More than 3GB/day → Premium Plan
# * 1GB to 3GB/day → Standard Plan
# * Less than 1GB/day → Basic Plan

# Write a Python program to recommend a plan.

# Input:
# Enter daily data usage: 0.8

# Output:
# Recommended Plan: Basic Plan

usage = float(input("Enter daily data usage: "))

if usage > 3:
    plan = "Premium Plan"
elif usage >= 1:
    plan = "Standard Plan"
else:
    plan = "Basic Plan"

print("Recommended Plan:", plan)