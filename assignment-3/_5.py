# Assignment 5: Average Marks Calculator

# Write a Python program that:

# Accepts marks of 3 subjects.
# Calculates average.

# Input:
# Marks = 80, 90, 70

# Output:
# Average = 80.0


mark1 = float(input("Enter marks of subject 1: "))
mark2 = float(input("Enter marks of subject 2: "))
mark3 = float(input("Enter marks of subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print("Average =", average)