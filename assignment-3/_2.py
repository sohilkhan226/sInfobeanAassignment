# Assignment 2: Salary Calculator

# Write a Python program that:

# Accepts daily wage and number of days.
# Calculates total salary.

# Input:
# Daily wage = 500
# Days = 26

# Output:
# Salary = 13000


daily_wage = float(input("Enter daily wage: "))
days = int(input("Enter number of days: "))

salary = daily_wage * days

print("Salary =", salary)