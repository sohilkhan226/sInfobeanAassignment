# Assignment 5: Salary Breakdown

# An employee wants to calculate salary per day and per hour.

# Input:
# Monthly salary = 36000
# Working days = 24
# Working hours per day = 8

# Expected Output:
# Salary per day = 1500.0
# Salary per hour = 187.5

monthly_salary = 36000
working_days = 24
working_hours = 8

salary_per_day = monthly_salary / working_days
salary_per_hour = salary_per_day / working_hours

print("Salary per day =", salary_per_day)
print("Salary per hour =", salary_per_hour)