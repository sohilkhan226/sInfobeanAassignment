# 5. Digit Alternating Sum System

# A coding system calculates alternating sum of digits (add, subtract, add...).

# Write a program to:

# Traverse digits from left to right
# Add first digit, subtract second, add third, and so on
# Display final alternating sum
# If result is positive → print Positive Pattern
# Else → print Negative Pattern

# Input:
# 1234

# Output:
# Result = -2
# Negative Pattern

# Input:
# 8642

# Output:
# Result = 8
# Positive Pattern


n_str = input()

# Extract digits
digits = []
for ch in n_str:
    digits.append(int(ch))

alt_sum = 0
i = 0
while i < len(digits):
    if i % 2 == 0:
        alt_sum += digits[i]  # Add 1st, 3rd, 5th...
    else:
        alt_sum -= digits[i]  # Subtract 2nd, 4th, 6th...
    i += 1

print("Result =", alt_sum)
if alt_sum > 0:
    print("Positive Pattern")
else:
    print("Negative Pattern")