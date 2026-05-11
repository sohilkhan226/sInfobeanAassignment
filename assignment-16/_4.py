# 4.
# 1. Digit Gap Consistency Checker

# A number analysis system checks whether the gap between digits follows a consistent pattern.

# Write a program to:

# Find the absolute difference between first two digits
# Compare this difference with all next adjacent digit differences
# If any difference is not equal to the first difference, stop using break
# Display:
# - Initial gap
# - Whether all gaps are same or not

# Input:
# 8642

# Output:
# Initial Gap = 2
# Consistent Pattern

# Input:
# 97531

# Output:
# Initial Gap = 2
# Consistent Pattern

# Input:
# 5321

# Output:
# Initial Gap = 2
# Pattern Break Detected


n_str = input()

# Extract digits
digits = []
for ch in n_str:
    digits.append(int(ch))

# Initial gap between first two digits
initial_gap = abs(digits[1] - digits[0])
consistent = True

i = 2
while i < len(digits):
    if abs(digits[i] - digits[i-1]) != initial_gap:
        consistent = False
        break
    i += 1

print("Initial Gap =", initial_gap)
if consistent:
    print("Consistent Pattern")
else:
    print("Pattern Break Detected")

