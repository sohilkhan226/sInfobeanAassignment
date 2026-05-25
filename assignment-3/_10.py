# Assignment 10: Percentage Calculator

# Write a Python program that:

# Accepts total marks and obtained marks.
# Calculates percentage.

# Input:
# Total = 500
# Obtained = 400

# Output:
# Percentage = 80%

total = 500
obtained = 400
print("percentage",400/500*100,"%")






total = float(input("Enter total marks: "))
obtained = float(input("Enter obtained marks: "))

percentage = (obtained / total) * 100

print("Percentage =", percentage, "%")