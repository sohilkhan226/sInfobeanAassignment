# 2. College Result Processing System


# A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

# * 90 and above → Grade A
# * 75 to 89 → Grade B
# * 60 to 74 → Grade C
# * 50 to 59 → Grade D
# * Below 50 → Fail

# Write a Python program to display the grade of a student.

# Input:
# Enter marks: 67

# Output:
# Grade: C

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)