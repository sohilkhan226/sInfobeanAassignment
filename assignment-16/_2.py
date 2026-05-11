# 2.
# Digit Order Break Analyzer

# A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

# Write a program to:

# Traverse the digits from left to right
# Check whether each digit is greater than the previous digit
# If the pattern breaks at any point, stop checking further using break
# Display the position where the order breaks (1-based index)
# If no break occurs, print Strictly Increasing Number

# Use loops and break wherever required.

# Input:
# 12357

# Output:
# Strictly Increasing Number

# Input:
# 12342

# Output:
# Break at position = 4
# Not Increasing Number

n_str = input()

# Extract digits
digits = []
for ch in n_str:
    digits.append(int(ch))

break_pos = -1
i = 1
while i < len(digits):
    if digits[i] <= digits[i-1]:
        break_pos = i  # 1-based index where increasing order stops
        break
    i += 1

if break_pos == -1:
    print("Strictly Increasing Number")
else:
    print("Break at position =", break_pos)
    print("Not Increasing Number")


