# 13. Employee Performance Appraisal System

# A company evaluates employees based on performance rating (1–5):

# * 5 → 25% salary hike
# * 4 → 20% salary hike
# * 3 → 10% salary hike
# * 2 → 5% salary hike
# * 1 → No hike
#   If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

# Write a Python program to calculate revised salary.

# Input:
# Enter salary: 18000
# Enter rating: 4

# Output:
# Revised Salary: ₹23600

salary = float(input("Enter salary: "))
rating = int(input("Enter rating: "))

if rating == 5:
    hike = salary * 25 / 100
elif rating == 4:
    hike = salary * 20 / 100
elif rating == 3:
    hike = salary * 10 / 100
elif rating == 2:
    hike = salary * 5 / 100
else:
    hike = 0

if salary < 20000 and rating >= 4:
    bonus = 2000
else:
    bonus = 0

revised_salary = salary + hike + bonus

print("Revised Salary: ₹" + str(int(revised_salary)))