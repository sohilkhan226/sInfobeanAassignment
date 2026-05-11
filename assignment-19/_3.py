# 3. Employee Bonus Distribution System
# A company provides bonuses based on years of experience.
# Experience >10 years → 30% bonus
# Experience >5 years → 20% bonus
# Otherwise → 10% bonus
# Write a program to calculate the total salary after adding bonus using inline if.


salary = float(input("Enter salary: "))
experience = int(input("Enter experience in years: "))

bonus = 30 / 100 if experience > 10 else 20 / 100 if experience > 5 else 10 / 100
total_salary = salary + salary * bonus

print("Total Salary =", total_salary)