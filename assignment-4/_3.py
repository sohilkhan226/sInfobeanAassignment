# Assignment 3: Student Marks Analysis

# A student wants to calculate total marks, average, and percentage from 5 subjects.

# Input:
# Marks = 78, 85, 90, 88, 80

# Expected Output:
# Total = 421
# Average = 84.2
# Percentage = 84.2


m1 = 78
m2 = 85
m3 = 90
m4 = 88
m5 = 80
total_marks = 500

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = total / total_marks * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)