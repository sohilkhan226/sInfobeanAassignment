# 1.
# Digit Frequency Balance Analyzer

# A data security system analyzes numeric IDs to check digit distribution patterns.

# For a given number, the system evaluates how frequently each digit appears.

# Write a program to:

# Count how many times each digit appears in the number
# Display only the digits that appear more than once
# Find the total count of repeated digits
# Find the digit with maximum frequency
# If no digit repeats, print Unique Number
# If at least one digit repeats, print Repeated Pattern Detected

# Use loops wherever required.

# Input:
# 1223451

# Output:
# Repeated Digits: 1 2
# Total Repeated Count = 4
# Max Frequency Digit = 1
# Repeated Pattern Detected


num_str = input()

# Step 1: Count frequency of each digit using loop
freq = [0] * 10
for ch in num_str:
    freq[int(ch)] += 1

# Step 2: Find repeated digits and total repeated count
repeated_digits = []
total_repeated = 0
for d in range(10):
    if freq[d] > 1:
        repeated_digits.append(d)
        total_repeated += freq[d]

# Step 3: Find digit with maximum frequency using loop
max_freq = 0
max_digit = -1
for d in range(10):
    if freq[d] > max_freq:
        max_freq = freq[d]
        max_digit = d

# Step 4: Display results
if not repeated_digits:
    print("Unique Number")
else:
    print("Repeated Digits:", end=" ")
    for d in repeated_digits:
        print(d, end=" ")
    print()
    print("Total Repeated Count =", total_repeated)
    print("Max Frequency Digit =", max_digit)
    print("Repeated Pattern Detected")

